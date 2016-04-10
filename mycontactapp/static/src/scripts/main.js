require('../../../../node_modules/bootstrap-sass/assets/stylesheets/_bootstrap.scss');
require('../styles/style.scss');
require('bootstrap-sass');
var $ = require('jquery');

$(document).ready(function(formErrors) {
    if (formErrors) {
        //$('.modal').modal('show');
        console.log('This function works!')
    }
});
