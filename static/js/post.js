// 에디터 컨테이너 요소를 가져옵니다.
const editorElement = document.querySelector('#editor');

// 에디터 인스턴스를 생성하고 초기화합니다.
const editor = new toastui.Editor({
    el: editorElement,
    initialEditType: 'wysiwyg', // WYSIWYG 모드로 시작합니다.
    previewStyle: 'vertical', // 미리보기 스타일을 수직 방향으로 설정합니다.
});

const form = document.querySelector('form');

form.addEventListener('submit', function (event) {
    event.preventDefault(); // 기본 동작인 폼의 서버 전송을 막습니다.

    const formData = new FormData(form);
    formData.append('contents', editor.getMarkdown()); // TOAST-UI Editor의 내용을 폼 데이터에 추가합니다.

    fetch(form.action, {
        method: form.method,
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            // 서버 응답에 대한 처리를 수행합니다.
            location.replace({ % url 'boards:index' %})
        })
        .catch(error => {
            // 오류 처리를 수행합니다.
            location.replace({ % url'boards:index' %})
        });
});