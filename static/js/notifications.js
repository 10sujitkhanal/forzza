let csrfmiddlewaretoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;

let likeCommentNotificationSocket = new ReconnectingWebSocket(
    'ws://' + window.location.host +
    '/ws/like-comment-notification/');


function fetchNotifications() {
    likeCommentNotificationSocket.send(JSON.stringify({'command': 'fetch_like_comment_notifications'}));
}

function createLikeCommentNotification(notification) {
    let single = `<li>
                        <a href="#" title="">
                            
                            <div class="mesg-meta">
                                <span>${notification.actor.username} ${notification.verb}</span>
                            </div>
                        </a>
                    </li>`;
    $('#like-comment-menu').prepend(single);
}

likeCommentNotificationSocket.onopen = function (e) {
    fetchNotifications();
};

likeCommentNotificationSocket.onmessage = function (event) {
    let data = JSON.parse(event.data);
    if (data['command'] === 'notifications') {
        let notifications = JSON.parse(data['notifications']);
        $('#total-like-comment-notifications').text(notifications.length);
        for (let i = 0; i < notifications.length; i++) {
            createLikeCommentNotification(notifications[i]);
        }
    } else if (data['command'] === 'new_like_comment_notification') {
        let notification = $('#total-like-comment-notifications');
        notification.text(parseInt(notification.text()) + 1);
        createLikeCommentNotification(JSON.parse(data['notification']));
    }
};

$('#mark-like-comment-notifications-as-read').click(function () {

    let url = $(this).data('url');

    $.ajaxSetup({
        headers: {
            'X-CSRFToken': csrfmiddlewaretoken
        }
    });

    $.ajax({
        type: 'POST',
        url: url,
        dataType: 'json',
        success: function (res) {
            console.log(res);
            if (res.status === false) {
            }
            if (res.status === true) {}

        },
        error: function (err) {
            console.log(err);
        }
    });
});
