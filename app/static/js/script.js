function updateTime() {
        const now = new Date();

            // Форматирование только часов и минут
            const formattedTime = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
            document.getElementById('user-time').innerText = formattedTime;

            // Форматирование дня недели, числа и месяца
            const formattedDate = now.toLocaleDateString('ru-RU', { weekday: 'long', day: 'numeric', month: 'long' });
            document.getElementById('user-date').innerText = formattedDate.charAt(0).toUpperCase() + formattedDate.slice(1);
    }

    // Обновляем время каждую секунду
    setInterval(updateTime, 1000);

function updateTemperature() {
    fetch('/get_temperature')
        .then(response => response.json())
        .then(data => {
            console.log('Полученные данные:', data);
            document.getElementById('weather').innerText = `${data.temp}°C`;
        })
        .catch(error => console.error('Error fetching temperature:', error));
}

// Обновляем время каждую секунду
setInterval(updateTime, 1000);

// Обновляем время и температуру при загрузке страницы
window.onload = function() {
    updateTime();
    updateTemperature();
}

// Обновляем температуру каждые 30 минут
setInterval(updateTemperature, 1800000);

