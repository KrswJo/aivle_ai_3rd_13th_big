const form = document.querySelector('form');

form.addEventListener('submit', function(event) {
event.preventDefault(); // 기본 동작인 폼의 서버 전송을 막습니다.

const formData = new FormData(form);
formData.append('content', editor.getMarkdown()); // TOAST-UI Editor의 내용을 폼 데이터에 추가합니다.

fetch(form.action, {
method: form.method,
body: formData
})
.then(response => response.json())
.then(data => {
alert("정상적으로 작성되었습니다.");
})
.catch(error => {
alert("알 수 없는 오류로 인하여 작성되지 않았습니다.");
});
});