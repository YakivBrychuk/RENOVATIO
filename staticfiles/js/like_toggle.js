document.addEventListener('DOMContentLoaded', function () {
    const heartIcon = document.getElementById('heartIcon');
    const likeButton = document.getElementById('likeButton');
    let isLiked = '{{ liked }}' === 'True';

    // Hover effect
    heartIcon.addEventListener('mouseover', function () {
        if (!isLiked) {
            heartIcon.style.fill = '#00FF76';
        }
    });

    heartIcon.addEventListener('mouseout', function () {
        if (!isLiked) {
            heartIcon.style.fill = '#020C22';
        }
    });

    // Toggle Like  
    likeButton.addEventListener('click', function () {
        isLiked = !isLiked;
        heartIcon.style.fill = isLiked ? '#00FF76' : '#020C22';
        // Optional: Send an AJAX request to update like count in the backend.
    });
});
