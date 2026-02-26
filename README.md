# The-whisper-of-Life markdown
# Second Pair of Eyes — ICU Early Warning System

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.9+-green)
![Flask](https://img.shields.io/badge/flask-2.3+-lightgrey)
![License](https://img.shields.io/badge/license-MIT-orange)

## 👁️ О проекте

**Second Pair of Eyes** — это система раннего предупреждения ухудшения состояния пациентов для отделений реанимации и интенсивной терапии. Проект разработан для хакатона Harvard Health Systems Innovation Lab 2026.

> *"Каждую неделю я вижу пациентов, которых привозят к нам из обычных отделений, когда уже слишком поздно. Этот проект — способ дать медсестрам вторую пару глаз."* — Гера, медсестра ICU

### Проблема
В обычных отделениях медсестры проверяют пациентов дискретно (например, раз в 4-6 часов). За это время состояние пациента может критически ухудшиться без видимых признаков. К моменту обнаружения проблемы часто уже поздно — развивается септический шок или остановка сердца.

### Решение
Наша система анализирует витальные показатели в реальном времени, рассчитывает ранговую оценку ухудшения (Early Warning Score) и отправляет оповещения при выявлении рисков.

## 🚀 Быстрый старт

### Требования
- Python 3.9 или выше
- pip (менеджер пакетов)

### Установка

1. **Клонируйте репозиторий**
```bash
git clone https://github.com/yourusername/second-pair-of-eyes.git
cd second-pair-of-eyes
pip install -r requirements.txt
python app.py
http://localhost:5000
🏗️ Архитектура
text
├── app.py                 # Основное Flask приложение
├── models/
│   └── ews_calculator.py  # Логика расчета риска (NEWS2)
├── templates/
│   └── index.html         # Пользовательский интерфейс
├── static/                 # CSS, JavaScript файлы
├── requirements.txt        # Зависимости
└── README.md               # Документация
Алгоритм оценки
Система использует модифицированную шкалу NEWS2 (National Early Warning Score 2) , адаптированную под условия ICU:

Пульс (уд/мин)

Систолическое давление (mmHg)

Частота дыхания (в мин)

Температура (°C)

Сатурация SpO2 (%)

Кислородная поддержка (да/нет)

Уровень сознания (AVPU)

Уровни риска
Баллы	Уровень	Цвет	Действие
0-2	Низкий	🟢 Зеленый	Плановое наблюдение
3-4	Средний	🟡 Желтый	Повторная оценка через 1 час
5-6	Высокий	🟠 Оранжевый	Срочный осмотр врача
7+	Критический	🔴 Красный	Немедленный перевод в ICU
🎯 Для хакатона
Наша команда
Гера — студентка 4 курса БФУ им. Канта, медсестра ICU (Россия)

Денис — партнер по команде, работает в ICU (Беларусь)

Уникальность нашего подхода
Реальный клинический опыт — мы работаем в реанимации и видим проблему изнутри

Международная перспектива — Россия и Беларусь, одни и те же вызовы

Человекоцентричность — мы создаем инструмент для медсестер, наших коллег

Доказательная база — алгоритм основан на валидированной шкале NEWS2

Демонстрационные случаи
Приложение включает три предустановленных сценария:

✅ Норма — стабильный пациент

⚠️ Средний риск — требует внимания

🚨 Критический — срочное вмешательство

📊 Презентационные материалы
Ключевые сообщения
Проблема: 40% предотвратимых смертей связаны с поздним выявлением ухудшения

Решение: AI-ассистированная система раннего предупреждения

Доказательства: Основано на валидированной шкале NEWS2

Масштабируемость: От маленькой районной больницы до крупного медицинского центра

🛠️ Технологии
Backend: Python, Flask

Frontend: HTML5, CSS3, JavaScript

Визуализация: Plotly

ML/AI: scikit-learn (для расширенной версии)

📝 Лицензия
MIT License — свободное использование, модификация и распространение

🤝 Контакты
По всем вопросам: [geragaffar@mail.ru]

Second Pair of Eyes — потому что одна пара глаз не всегда успевает заметить

text

---

 `LICENSE`**
MIT License

Copyright (c) 2026 Gera & Denis

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
