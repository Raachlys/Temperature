from flask import Flask, render_template, request

app = Flask(__name__)

# Функції для конвертації температур
def to_celsius(value, unit):
    if unit == 'fahrenheit':
        return (value - 32) * 5/9
    elif unit == 'kelvin':
        return value - 273.15
    return value  # Якщо вже в Цельсії, повертаємо без змін

def to_fahrenheit(value, unit):
    if unit == 'celsius':
        return (value * 9/5) + 32
    elif unit == 'kelvin':
        return (value - 273.15) * 9/5 + 32
    return value  # Якщо вже у Фаренгейті, повертаємо без змін

def to_kelvin(value, unit):
    if unit == 'celsius':
        return value + 273.15
    elif unit == 'fahrenheit':
        return (value - 32) * 5/9 + 273.15
    return value  # Якщо вже в Кельвіні, повертаємо без змін

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        temperature = float(request.form['temperature'])
        unit = request.form['unit']
        
        # Конвертація температури в усі одиниці
        celsius = to_celsius(temperature, unit)
        fahrenheit = to_fahrenheit(temperature, unit)
        kelvin = to_kelvin(temperature, unit)

        result = {
            'original': temperature,
            'unit': unit,
            'celsius': round(celsius, 2),
            'fahrenheit': round(fahrenheit, 2),
            'kelvin': round(kelvin, 2)
        }
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

