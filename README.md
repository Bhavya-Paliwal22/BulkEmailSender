# 📧 Bulk Email Sender

A web-based Bulk Email Sender application built using Flask and SMTP that allows users to send emails to multiple recipients at once.

## 🚀 Features

- Send emails to multiple recipients
- Simple and user-friendly interface
- Gmail SMTP integration
- Secure authentication using App Passwords
- Fast bulk email delivery

## 🛠️ Tech Stack

### Frontend
- HTML
- CSS

### Backend
- Python
- Flask

### Email Service
- SMTP
- Gmail App Password Authentication

## 📂 Project Structure

```text
BulkEmailSender/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

## ⚙️ How It Works

1. User enters Gmail address and App Password.
2. Adds recipient email addresses.
3. Writes email subject and message.
4. Application connects to Gmail SMTP server.
5. Emails are delivered to all recipients.

## 🔒 Security

- Uses Gmail App Password instead of normal Gmail password.
- SMTP connection secured using TLS encryption.

## 🎯 Learning Outcomes

- Flask Routing
- Form Handling
- SMTP Integration
- Email Automation
- Web Application Development
