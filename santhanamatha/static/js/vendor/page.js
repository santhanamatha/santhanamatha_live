
$(document).on('click', '.email_us' ,function(){
console.log("called")
   $('#compose-email-modal').addClass("is-active");
})

setTimeout(function () {
    if ($('.alert').length > 0) {
        $('.alert').remove();
    }
}, 5000)
$(function () {
    var pathName = document.location.pathname;
    window.onbeforeunload = function () {
        var scrollPosition = $(document).scrollTop();
        sessionStorage.setItem("scrollPosition_" + pathName, scrollPosition.toString());
    }
    if (sessionStorage["scrollPosition_" + pathName]) {
        $(document).scrollTop(sessionStorage.getItem("scrollPosition_" + pathName));
    }
});

window.Parsley.addValidator('uppercase', {
  requirementType: 'number',
  validateString: function(value, requirement) {
    var uppercases = value.match(/[A-Z]/g) || [];
    return uppercases.length >= requirement;
  },
  messages: {
    en: 'Your password must contain at least (%s) uppercase letter.'
  }
});
//has lowercase
window.Parsley.addValidator('lowercase', {
  requirementType: 'number',
  validateString: function(value, requirement) {
    var lowecases = value.match(/[a-z]/g) || [];
    return lowecases.length >= requirement;
  },
  messages: {
    en: 'Your password must contain at least (%s) lowercase letter.'
  }
});
window.Parsley.addValidator('registerno', {
  requirementType: 'string',
     requirementType: 'string',
            validateString: function (value, requirement) {
                regex = '/^([L|U]{1})([0-9]{5})([A-Za-z]{2})([0-9]{4})([A-Za-z]{3})([0-9]{6})$;'
                return regex.test(value);
            },
            messages: {
                en: 'registration_no must have 21 characters'
            }
});
//has number
window.Parsley.addValidator('number', {
  requirementType: 'number',
  validateString: function(value, requirement) {
    var numbers = value.match(/[0-9]/g) || [];
    return numbers.length >= requirement;
  },
  messages: {
    en: 'Your password must contain at least (%s) number.'
  }
});
//has special char
window.Parsley.addValidator('special', {
  requirementType: 'number',
  validateString: function(value, requirement) {
    var specials = value.match(/[^a-zA-Z0-9]/g) || [];
    return specials.length >= requirement;
  },
  messages: {
    en: 'Your password must contain at least (%s) special characters.'
  }
});
window.Parsley.addValidator('validateFullWidthCharacters', {
    requirementType: 'string',
    validateString: function (value, requirement) {
        regex = /^([a-z0-9_\.-]+\@[\da-z\.-]+\.[a-z\.]{2,6})$/gm;
        return regex.test(value);
    },
    messages: {
        en: 'Please enter a valid email address.'
    }
});
$("form").on('submit', function(event) {
    // validate form with parsley.
    $(this).parsley().validate();

    // if this form is valid
    if ($(this).parsley().isValid()) {
        // show alert message
         $(this).find("button[type='submit']").prop('disabled',true);
        return true;
    }
   return false;
    // prevent default so the form doesn't submit. We can return true and
    // the form will be submited or proceed with a ajax request.
    event.preventDefault();
});

$(document).on('click', '.toggle-password', function() {
    $(this).toggleClass("fa-eye fa-eye-slash");
    var input = $('input[name="password"]')
    input.attr('type') === 'password' ? input.attr('type','text') : input.attr('type','password')
});

$(function(){
    var current = location.pathname;
    $('ul.menu-list li.menu-item a').each(function(){
        var $this = $(this);
        // if the current path is like this link, make it active
        if($this.attr('href').indexOf(current) !== -1){
            $('ul.menu-list li.menu-item').removeClass('is-active');
            $this.parent('li').addClass('is-active');
        }
    })
})

     // FOR CMA FORM TABS CLICK ACTIVE CLASS
     $(function(){
        var current = location.pathname;
        $('.tabs .tab-links li a').each(function(){
            var $this = $(this);
            // if the current path is like this link, make it active
            if($this.attr('href').indexOf(current) !== -1){
                $('.tabs .tab-links li').removeClass('active');
                $this.parent('li').addClass('active');
            }
        })
    })



$(document).ready(function() {
    var parsleyConfig = {
        errorsContainer: function(parsleyField) {
            var fieldSet = parsleyField.$element.closest('fieldset');

            if (fieldSet.length > 0) {
                return fieldSet.find('.custom_errors_contaniner');
            }

            return parsleyField;
        }
    };


    $("form").parsley(parsleyConfig);
});