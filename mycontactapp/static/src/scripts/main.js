require('../../../../node_modules/bootstrap-sass/assets/stylesheets/_bootstrap.scss');
require('../styles/style.scss');
require('bootstrap-sass');
var $ = require('jquery');

$(document).ready(function() {
    if ($('.form-errors').length) {
        $('.modal:has(.form-errors)').modal('show');
    }
});
