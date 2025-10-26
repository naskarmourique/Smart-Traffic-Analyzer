document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form');
    const body = document.querySelector('body');

    forms.forEach(form => {
        form.addEventListener('submit', function() {
            body.classList.add('loading');
        });
    });
});
