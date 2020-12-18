var notify_badge_class;
var notify_menu_class;
var notify_api_url;
var notify_fetch_count;
var notify_unread_url;
var notify_mark_all_unread_url;
var notify_refresh_period = 15000;
var consecutive_misfires = 0;
var registered_functions = [];

function fill_notification_badge(data) {
    var badges = document.getElementsByClassName(notify_badge_class);
    if (badges) {
        for(var i = 0; i < badges.length; i++){
            badges[i].innerHTML = data.unread_count;
        }
    }
}

var MONTHS = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
];


function getFormattedDate(date, prefomattedDate = false, hideYear = false) {
    const day = date.getDate();
    const month = MONTHS[date.getMonth()];
    const year = date.getFullYear();
    const hours = date.getHours();
    let minutes = date.getMinutes();
    let ampm = hours >= 12 ? 'pm' : 'am';

    if (minutes < 10) {
        // Adding leading zero to minutes
        minutes = `0${minutes}`;
    }

    if (prefomattedDate) {
        // Today at 10:20
        // Yesterday at 10:20
        return `${prefomattedDate} at ${hours}:${minutes} ${ampm}`;
    }

    if (hideYear) {
        // 10. January at 10:20
        return `${day}. ${month} at ${hours}:${minutes} ${ampm}`;
    }

    // 10. January 2017. at 10:20
    return `${day}. ${month} ${year}. at ${hours}:${minutes} ${ampm}`;
}


// --- Main function
function timeAgo(dateParam) {
    if (!dateParam) {
        return null;
    }

    const date = typeof dateParam === 'object' ? dateParam : new Date(dateParam);
    const DAY_IN_MS = 86400000; // 24 * 60 * 60 * 1000
    const today = new Date();
    const yesterday = new Date(today - DAY_IN_MS);
    const seconds = Math.round((today - date) / 1000);
    const minutes = Math.round(seconds / 60);
    const isToday = today.toDateString() === date.toDateString();
    const isYesterday = yesterday.toDateString() === date.toDateString();
    const isThisYear = today.getFullYear() === date.getFullYear();


    if (seconds < 5) {
        return 'now';
    } else if (seconds < 60) {
        return `${seconds} seconds ago`;
    } else if (seconds < 90) {
        return 'about a minute ago';
    } else if (minutes < 60) {
        return `${minutes} minutes ago`;
    } else if (isToday) {
        return getFormattedDate(date, 'Today'); // Today at 10:20
    } else if (isYesterday) {
        return getFormattedDate(date, 'Yesterday'); // Yesterday at 10:20
    } else if (isThisYear) {
        return getFormattedDate(date, false, true); // 10. January at 10:20
    }

    return getFormattedDate(date); // 10. January 2017. at 10:20
}

function fill_notification_list(data) {
    var menus = document.getElementsByClassName('drop-content');
    if (menus) {
        var messages = data.unread_list.map(function (item) {
            var message = "";
            if(typeof item.actor !== 'undefined'){
                message = item.actor;
            }
            if(typeof item.verb !== 'undefined'){
                message = message + " " + item.verb;
            }
            if(typeof item.target !== 'undefined'){
                message = message + " " + item.target;
            }
            if(typeof item.timestamp !== 'undefined'){
                message = message + " " + item.timestamp;
            }
            return '<li class="row card bg-light text-dark"><div class="col-md-3 col-sm-3 col-xs-3"><div class="notify-img"><img src="http://placehold.it/45x45" alt=""></div></div><div class="col-md-9 col-sm-9 col-xs-9 pd-l0"><span>'+ item.actor + ' ' + item.verb + '</span><span class="time">'+ ' '+ timeAgo(item.timestamp) + ' ago</span></div></li><br>';
        }).join('')

        for (var i = 0; i < menus.length; i++){
            menus[i].innerHTML = messages;
        }
    }
}



notify_menu_class = "drop-content";

function my_special_notification_callback(data) {
    let menus = document.getElementsByClassName(notify_menu_class);
    if (menus) {
        let messages = data.unread_list.map(function (item) {
            let unread = '';
            let username = '';
            let verb = '';
            let timestamp = '';
            if (typeof item.unread !== 'undefined' && item.unread === true) {
                unread = 'alert alert-primary';
            }
            if (typeof item.actor !== 'undefined') {
                username = item.actor;
            }
            if (typeof item.verb !== 'undefined') {
                verb = item.verb;
            }
            if (typeof item.timestamp !== 'undefined') {
                timestamp = item.timestamp;
            }
            return '<li class="row ' + unread + '">\n' +
                '                                    <div class="col-md-3 col-sm-3 col-xs-3">\n' +
                '                                        <div class="notify-img">\n' +
                '                                            <img src="http://placehold.it/45x45" alt="">\n' +
                '                                        </div>\n' +
                '                                    </div>\n' +
                '                                    <div class="col-md-9 col-sm-9 col-xs-9 pd-l0">\n' +
                '                                        <p><strong>' + username + '</strong> ' + verb + '</p>\n' +
                '                                        <a href="" class="rIcon"><i class="fa fa-dot-circle-o"></i></a>\n' +
                '                                        <p class="time">' + timeAgo(timestamp) + '</p>\n' +
                '                                    </div>\n' +
                '                                </li>';
            // return '<li class="row ' + unread + '">' + message + '</li>';
        }).join('');

        for (let i = 0; i < menus.length; i++) {
            menus[i].innerHTML = messages;
        }
    }
}

function register_notifier(func) {
    registered_functions.push(func);
}

function fetch_api_data() {
    if (registered_functions.length > 0) {
        //only fetch data if a function is setup
        var r = new XMLHttpRequest();
        r.addEventListener('readystatechange', function(event){
            if (this.readyState === 4){
                if (this.status === 200){
                    consecutive_misfires = 0;
                    var data = JSON.parse(r.responseText);
                    registered_functions.forEach(function (func) { func(data); });
                }else{
                    consecutive_misfires++;
                }
            }
        })
        r.open("GET", notify_api_url+'?max='+notify_fetch_count, true);
        r.send();
    }
    if (consecutive_misfires < 10) {
        setTimeout(fetch_api_data,notify_refresh_period);
    } else {
        var badges = document.getElementsByClassName(notify_badge_class);
        if (badges) {
            for (var i = 0; i < badges.length; i++){
                badges[i].innerHTML = "!";
                badges[i].title = "Connection lost!"
            }
        }
    }
}

setTimeout(fetch_api_data, 1000);

