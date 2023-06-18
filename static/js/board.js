function parseContents(target) {
            contents = target.replaceAll("<br>", "\n")
                .replaceAll("&gt;", ">")
                .replaceAll("&lt;", "<")
                .replaceAll("&quot;", "")
                .replaceAll("&nbsp;", " ")
                .replaceAll("&amp;", "&");

            return contents
        }
function setContents(selector, contents) {
    let viewer = document.querySelector(selector);
    viewer.innerHTML = contents;
}