$(document).ready(function() {
    $('#registrationForm').submit(function(event) {
        event.preventDefault();
        let isValid = true;

        // Validate name
        if ($('#name').val().trim() === '') {
            $('#name').addClass('is-invalid');
            isValid = false;
        } else {
            $('#name').removeClass('is-invalid');
        }

        // Validate email
        if ($('#email').val().trim() === '' || !isValidEmail($('#email').val().trim())) {
            $('#email').addClass('is-invalid');
            isValid = false;
        } else {
            $('#email').removeClass('is-invalid');
        }

        // Validate phone
        if ($('#phone').val().trim() === '' || !isValidPhone($('#phone').val().trim())) {
            $('#phone').addClass('is-invalid');
            isValid = false;
        } else {
            $('#phone').removeClass('is-invalid');
        }

        if (isValid) {
            alert('Form submitted successfully!');
            // Here you can add code to submit the form to a server
        }
    });

    function isValidEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    function isValidPhone(phone) {
        const re = /^[0-9]{10}$/;
        return re.test(phone);
    }
});
