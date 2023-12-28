$('.nav-link').on('click', function(){

    var target = $(this).attr('href')

    $('.nav-link, .active').removeClass('active')

    $('.active, .show').removeClass('active show')

    $(this).addClass('active')

    $(`${target}`).addClass('active show')
    
    // console.log(target)

})