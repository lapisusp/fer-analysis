$(document).ready(function () {
    var videos = ['small.mp4', 'dolbycanyon.mp4', 'grb_2.mp4'];
    var pos = 0;

    if (localStorage.getItem('posVideo')) {
        pos = parseInt(localStorage.getItem('posVideo'));
    }
    else localStorage.setItem('posVideo', 0);

    $('video').attr('src', 'videos/' + videos[pos]);
    $('video').attr('autoplay', 'true');
    $('video').trigger('play');
    $('video').on('ended', function () {
        if (pos < videos.length) {
            localStorage.setItem('posVideo', pos + 1);
            location.reload();
        }
    });
});