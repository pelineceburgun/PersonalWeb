document.getElementById('referenceForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const form = document.getElementById('referenceForm');
    const referencesList = document.getElementById('referencesList');
    const nameInput = document.getElementById('name');
    const imageInput = document.getElementById('image');
    const messageInput = document.getElementById('message');

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        const name = nameInput.value;
        const image = imageInput.value;
        const message = messageInput.value;

        const referenceItem = document.createElement('div');
        referenceItem.classList.add('reference-item');

        const referenceContent = `
        <h3>${name} - ${name}</h3>
        <p>${message}</p>
    `;

        referenceItem.innerHTML = referenceContent;
        referencesList.appendChild(referenceItem);

        form.reset();
    });
})
document.addEventListener('DOMContentLoaded', function() {
            const slides = document.getElementById('slides');
            const prevButton = document.getElementById('prev');
            const nextButton = document.getElementById('next');

            let currentIndex = 0;

            function showSlide(index) {
                const slideWidth = slides.children[0].clientWidth;
                slides.style.transform = `translateX(${-index * slideWidth}px)`;
            }

            prevButton.addEventListener('click', function() {
                currentIndex = (currentIndex > 0) ? currentIndex - 1 : slides.children.length - 1;
                showSlide(currentIndex);
            });

            nextButton.addEventListener('click', function() {
                currentIndex = (currentIndex < slides.children.length - 1) ? currentIndex + 1 : 0;
                showSlide(currentIndex);
            });


            setInterval(function() {
                currentIndex = (currentIndex < slides.children.length - 1) ? currentIndex + 1 : 0;
                showSlide(currentIndex);
            }, 3000);
        });




