var cardIndex = 0;

    function loadCard() {
        var cardContainer = document.getElementById('cardContainer');
        cardContainer.classList.remove('hidden');
        var card = createCard();
        cardContainer.appendChild(card);
    }
    
    function createCard() {
        var flipCard = document.createElement('div');
        flipCard.classList.add('flip-card');
        flipCard.style.width = '300px';
        flipCard.style.height = '400px';
        flipCard.style.fontFamily = 'sans-serif';
        flipCard.style.borderRadius = '1rem';
        flipCard.style.overflowY = 'scroll';
        flipCard.style.border = '1px solid transparent';
        
        flipCard.setAttribute('onclick', "this.classList.toggle('clicked')");
        
        var flipCardInner = document.createElement('div');
        flipCardInner.classList.add('flip-card-inner');
        
        var flipCardFront = document.createElement('div');
        flipCardFront.classList.add('flip-card-front');
        flipCardFront.style.backgroundImage = "url('https://www.hipstersofthecoast.com/wp-content/uploads/2023/06/en_8e6a0736e8.png')";
        flipCardFront.style.backgroundSize = 'contain';
        flipCardFront.style.backgroundPosition = 'center';
        flipCardFront.style.height = '100%';
        
        var flipCardBack = document.createElement('div');
        flipCardBack.classList.add('flip-card-back');
        flipCardBack.style.backgroundImage = "url('https://i.imgur.com/LdOBU1I.jpeg')";
        flipCardBack.style.backgroundSize = 'contain';
        flipCardBack.style.backgroundPosition = 'center';
        flipCardBack.style.height = '100%';
        flipCardBack.style.opacity = '0.5';
        
        var backContent = document.createElement('div');
        backContent.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
        var backText = document.createElement('p');
        backText.classList.add('text-white');
        backText.textContent = 'Card Details:';
        backContent.appendChild(backText);
        flipCardBack.appendChild(backContent);
        
        flipCardInner.appendChild(flipCardFront);
        flipCardInner.appendChild(flipCardBack);
        flipCard.appendChild(flipCardInner);
        
        cardIndex++;
        return flipCard;
    }

    function deleteCard() {
        var cardContainer = document.getElementById('cardContainer');
        var lastCard = cardContainer.lastElementChild;
        if (lastCard) {
            cardContainer.removeChild(lastCard);
        }
    }