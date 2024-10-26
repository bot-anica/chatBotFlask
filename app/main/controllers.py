from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from textblob import TextBlob

from app import db, groq_client
from app.main.forms import NewChatForm, MessageForm
from app.models import Message, Chat


def _analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return 'positive'
    elif polarity < 0:
        return 'negative'
    else:
        return 'neutral'


def _add_message(chat_id, text):
    new_message_emotion = _analyze_sentiment(text)

    new_message = Message(text=text, chat_id=chat_id, emotion=new_message_emotion)
    db.session.add(new_message)
    db.session.commit()

    answer_completion = groq_client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Based on the sentiment analysis result, the chatbot should respond differently for each category."
                           f"- Positive: Give an encouraging reply.\n"
                           f"- Negative: Apologize or offer help.\n"
                           f"- Neutral: Ask how it can help further.\n"
                           f"It should also be in the same language as the question.\n"
                           f"My question is: {text}"
                           f"Don't write your thoughts on the screen, just respond.\n"
                           f"If you got unexpected question please respond with 'I’m not sure I understand that.'.",
            }
        ],
        model="llama3-8b-8192",
    )

    new_message = Message(text=answer_completion.choices[0].message.content, chat_id=chat_id, author="bot")
    db.session.add(new_message)
    db.session.commit()


def _generate_chat_title(question):
    question_completion = groq_client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Give a title to this question conversation {question}. It should consist of one short sentence. It should also be in the same language as the question. It should be without quotes.",
            }
        ],
        model="llama3-8b-8192",
    )

    return question_completion.choices[0].message.content


def inject_chats():
    all_chats = Chat.query.all()
    return {'all_chats': all_chats}


def index():
    form = NewChatForm()

    if form.validate_on_submit():
        new_chat_title = _generate_chat_title(form.question.data)

        new_chat = Chat(title=new_chat_title, user_id=current_user.id)
        db.session.add(new_chat)
        db.session.commit()
        chat_id = new_chat.id

        _add_message(chat_id, form.question.data)
        flash('Chat created!')
        return redirect(url_for('main.chat', chat_id=chat_id))

    return render_template('main/index.html', title='Home', form=form)


def chat(chat_id):
    chat_data = Chat.query.get(chat_id)
    form = MessageForm()

    if form.validate_on_submit():
        _add_message(chat_id, form.text.data)
        flash('Message sent!')
        return redirect(url_for('main.chat', chat_id=chat_id))

    return render_template('main/chat.html', chat=chat_data, form=form)
