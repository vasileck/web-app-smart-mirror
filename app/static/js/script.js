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


// Обновляем температуру каждые 30 минут
setInterval(updateTemperature, 1800000);

function toggleForm() {
            const form = document.getElementById('add-form');
            text = document.getElementById('add-btn');
            if (form.style.display === 'none' || form.style.display === '') {
                form.style.display = 'block';  // Показываем форму
                document.getElementById('add-btn').innerText = 'Закрыть форму'
            } else {
                form.style.display = 'none';  // Скрываем форму
                document.getElementById('add-btn').innerText = 'Добавить запись';
            }
}

function toggleStatus(purchaseId) {
            fetch(`/update/${purchaseId}`, {
                method: 'POST'
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                // Если статус успешно изменен, обновляем интерфейс
                const checkbox = document.getElementById(`checkbox-${purchaseId}`);
                checkbox.checked = data.active;
                const text = checkbox.nextElementSibling;
                if (data.active) {
                    text.style.textDecoration = "line-through";
                    text.style.color = "#999";
                } else {
                    text.style.textDecoration = "none";
                    text.style.color = "#fff";
                }
            });
}

function deleteItem(purchaseId) {
            if (confirm('Вы уверены, что хотите удалить эту запись?')) {
                fetch(`/delete/${purchaseId}`, {
                    method: 'POST'
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        // Удаляем элемент из DOM
                        const itemElement = document.getElementById(`checkbox-${purchaseId}`).parentElement;
                        itemElement.remove();
                    } else {
                        alert('Ошибка при удалении записи.');
                    }
                })
                .catch(error => console.error('Ошибка удаления:', error));
            }
        }

window.onload = function() {
    updateTime();
    updateTemperature();
}