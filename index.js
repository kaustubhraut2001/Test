fetch('https://emojihub.yurace.pro/api/all')
    .then(response => response.json())
    .then(emojis => {
        const emojiContainer = document.getElementById('emoji-container');

        emojis.forEach(emoji => {
            const emojiCard = document.createElement('div');
            emojiCard.classList.add('emoji-card');

            const emojiElement = document.createElement('div');
            emojiElement.classList.add('emoji');
            emojiElement.innerHTML = emoji.htmlCode;

            const detailsElement = document.createElement('div');
            detailsElement.classList.add('details');

            const nameElement = document.createElement('div');
            nameElement.classList.add('name');
            nameElement.textContent = emoji.name;

            const categoryElement = document.createElement('div');
            categoryElement.classList.add('category');
            categoryElement.textContent = emoji.category;

            const groupElement = document.createElement('div');
            groupElement.classList.add('group');
            groupElement.textContent = emoji.group;

            detailsElement.appendChild(nameElement);
            detailsElement.appendChild(categoryElement);
            detailsElement.appendChild(groupElement);

            emojiCard.appendChild(emojiElement);
            emojiCard.appendChild(detailsElement);

            emojiContainer.appendChild(emojiCard);
        });
    })
    .catch(error => {
        console.log('Error fetching emoji details:', error);
    });