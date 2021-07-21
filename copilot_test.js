function calculateDaysBetween(begin, end) {
    var beginDate = new Date(begin);
    var endDate = new Date(end);
    var days = Math.round((endDate - beginDate) / (24 * 60 * 60 * 1000));
    return days;
}

function createColor() {
    var letters = '0123456789ABCDEF'.split('');
    var color = '#';
    for (var i = 0; i < 6; i++ ) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

function fetchTweetsByHashtag(hashtag, callback) {
    var url = "https://api.twitter.com/1.1/search/tweets.json?q=%23" + hashtag + "&count=100";
    $.getJSON(url, function(data) {
        var tweets = [];
        for (var i = 0; i < data.statuses.length; i++) {
            var tweet = data.statuses[i];
            tweets.push({
                id: tweet.id_str,
                text: tweet.text,
                user: tweet.user.screen_name,
                date: tweet.created_at,
                color: createColor()
            });
        }
        callback(tweets);
    });
}

//find the tweets with the most retweets
function findMostRetweetedTweets(tweets, callback) {
    var retweets = [];
    for (var i = 0; i < tweets.length; i++) {
        var tweet = tweets[i];
        var retweetsCount = 0;
        for (var j = 0; j < tweets.length; j++) {
            if (tweets[j].id == tweet.id) {
                retweetsCount++;
            }
        }
        retweets.push({
            id: tweet.id,
            text: tweet.text,
            user: tweet.user,
            date: tweet.date,
            retweets: retweetsCount,
            color: tweet.color
        });
    }
    retweets.sort(function(a, b) {
        return b.retweets - a.retweets;
    });
    callback(retweets);
}

function getStringLength(str) {
    var length = 0;
    for (var i = 0; i < str.length; i++) {
        if (str.charAt(i) == ' ') {
            length++;
        }
    }
    return length;
}

function    getGitHubUser(username) {
    var url = "https://api.github.com/users/" + username;
    $.getJSON(url, function(data) {
        var user = {
            name: data.name,
            username: data.login,
            avatar: data.avatar_url,
            location: data.location,
            company: data.company,
            email: data.email,
            bio: data.bio,
            followers: data.followers,
            following: data.following,
            public_repos: data.public_repos,
            public_gists: data.public_gists,
            created_at: data.created_at,
            updated_at: data.updated_at
        };
        callback(user);
    });
}