python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Second Pair of Eyes - ICU Early Warning System
Веб-приложение для раннего предупреждения ухудшения состояния пациентов

Основано на исследованиях NEWS2 и системах машинного обучения [citation:3][citation:8]
"""

from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os
from datetime import datetime
import plotly
import plotly.graph_objs as go
import numpy as np

from models.ews_calculator import EWSCalculator, DemoDataGenerator

# Инициализация приложения
app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')
CORS(app)

# Инициализация компонентов
ews_calculator = EWSCalculator()
demo_generator = DemoDataGenerator()

# Хранилище данных (в реальном приложении здесь была бы БД)
patients_db = {}
assessments_history = []


@app.route('/')
def index():
    """Главная страница приложения"""
    return render_template('index.html')


@app.route('/api/assess', methods=['POST'])
def assess_patient():
    """
    API endpoint для оценки состояния пациента
    """
    try:
        data = request.json
        patient_id = data.get('patient_id', 'unknown')
        
        # Извлекаем витальные показатели
        vital_signs = {
            'hr': int(data.get('hr', 0)),
            'sbp': int(data.get('sbp', 0)),
            'rr': int(data.get('rr', 0)),
            'temp': float(data.get('temp', 0)),
            'spo2': int(data.get('spo2', 0)),
            'o2': int(data.get('o2', 0)),
            'avpu': data.get('avpu', 'alert')
        }
        
        # Расчет EWS
        assessment = ews_calculator.calculate_ews(vital_signs)
        
        # Анализ динамики
        trend = ews_calculator.calculate_trend(patient_id, assessment)
        assessment['trend'] = trend
        
        # Сохраняем в историю
        assessments_history.append({
            'patient_id': patient_id,
            'timestamp': datetime.now().isoformat(),
            'score': assessment['score'],
            'vital_signs': vital_signs
        })
        
        return jsonify({
            'success': True,
            'assessment': assessment
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@app.route('/api/demo/<case_type>')
def get_demo_case(case_type):
    """
    Получение демонстрационного случая для презентации
    """
    case = demo_generator.generate_patient_case(case_type)
    return jsonify(case)


@app.route('/api/history/<patient_id>')
def get_patient_history(patient_id):
    """
    Получение истории оценок пациента
    """
    patient_assessments = [
        a for a in assessments_history 
        if a['patient_id'] == patient_id
    ][-10:]  # последние 10 оценок
    
    if not patient_assessments:
        return jsonify({'history': []})
    
    # Подготовка данных для графика
    timestamps = [a['timestamp'] for a in patient_assessments]
    scores = [a['score'] for a in patient_assessments]
    
    # Создание графика с помощью Plotly
    fig = go.Figure(data=go.Scatter(
        x=timestamps,
        y=scores,
        mode='lines+markers',
        line=dict(color='#0066cc', width=2),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title='Динамика состояния пациента',
        xaxis_title='Время',
        yaxis_title='Баллы EWS',
        hovermode='x'
    )
    
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return jsonify({
        'history': patient_assessments,
        'graph': graph_json
    })


@app.route('/api/stats')
def get_statistics():
    """
    Получение статистики по системе
    """
    total_assessments = len(assessments_history)
    
    if total_assessments == 0:
        return jsonify({
            'total': 0,
            'critical': 0,
            'high': 0,
            'medium': 0,
            'low': 0
        })
    
    # Анализ распределения рисков
    critical = sum(1 for a in assessments_history if a['score'] >= 7)
    high = sum(1 for a in assessments_history if 5 <= a['score'] <= 6)
    medium = sum(1 for a in assessments_history if 3 <= a['score'] <= 4)
    low = sum(1 for a in assessments_history if a['score'] < 3)
    
    return jsonify({
        'total': total_assessments,
        'critical': critical,
        'high': high,
        'medium': medium,
        'low': low,
        'critical_percent': round(critical/total_assessments*100, 1),
        'high_percent': round(high/total_assessments*100, 1),
        'medium_percent': round(medium/total_assessments*100, 1),
        'low_percent': round(low/total_assessments*100, 1)
    })


@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    """
    Сбор обратной связи от пользователей
    """
    data = request.json
    # В реальном приложении здесь сохранение в БД
    return jsonify({'success': True})


@app.route('/static/<path:path>')
def serve_static(path):
    """Обслуживание статических файлов"""
    return send_from_directory('static', path)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
