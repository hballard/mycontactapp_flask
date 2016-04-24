var $ = require('jquery');

$(document).ready(function() {
    if ($('.form-errors').length) {
        $('.modal:has(.form-errors)').modal('show');
    }
});
