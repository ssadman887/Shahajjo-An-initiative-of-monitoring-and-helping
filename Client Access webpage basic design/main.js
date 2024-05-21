document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var userId = document.getElementById('userId').value;
    var password = document.getElementById('password').value;
    var users = {
        'user1': {
            'password': 'pass1',
            'videoShareLink': 'http://10.33.22.206:5000/',
            'filesShareLink': 'http://10.33.22.101:8000/'
        },
        'user2': {
            'password': 'pass2',
            'videoShareLink': 'http://10.33.22.102:5000/',
            'filesShareLink': 'http://10.33.22.102:8000/'
        },
        'user3': {
            'password': 'pass3',
            'videoShareLink': 'http://10.33.22.103:5000/',
            'filesShareLink': 'http://10.33.22.103:8000/'
        }
    };

    if (users[userId] && users[userId].password === password) {
        document.getElementById('loginForm').style.display = 'none';
        document.getElementById('buttonContainer').classList.remove('hidden');
        document.getElementById('videoShareButton').onclick = function() { window.location.href = users[userId].videoShareLink; };
        document.getElementById('filesShareButton').onclick = function() { window.location.href = users[userId].filesShareLink; };
    } else {
        alert('Invalid credentials!');
    }
});
