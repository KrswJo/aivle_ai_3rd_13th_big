function DropFile(dropAreaId, fileListId) {
  let dropArea = document.getElementById(dropAreaId);
  let fileList = document.getElementById(fileListId);

  function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
  }

  function highlight(e) {
    preventDefaults(e);
    dropArea.classList.add("highlight");
  }

  function unhighlight(e) {
    preventDefaults(e);
    dropArea.classList.remove("highlight");
  }

  function handleDrop(e) {
    unhighlight(e);
    let dt = e.dataTransfer;
    let files = dt.files;

    handleFiles(files);

    const fileList = document.getElementById(fileListId);
    if (fileList) {
      fileList.scrollTo({ top: fileList.scrollHeight });
    }
  }

  function handleFiles(files) {
    files = [...files];
    files.forEach(previewFile);
  }

  function previewFile(file) {
    console.log(file);
    fileList.appendChild(renderFile(file));
  }

  function renderFile(file) {
    let fileDOM = document.createElement("div");
    fileDOM.className = "file";

    let thumbnail = document.createElement("div");
    thumbnail.className = "thumbnail";
    let img = document.createElement("img");
    img.src = URL.createObjectURL(file); // Use uploaded image file as thumbnail
    img.alt = "파일타입 이미지";
    img.className = "image";
    thumbnail.appendChild(img);
    fileDOM.appendChild(thumbnail);

    let details = document.createElement("div");
    details.className = "details";
    let header = document.createElement("header");
    header.className = "header";
    let name = document.createElement("span");
    name.className = "name";
    name.textContent = file.name;
    let size = document.createElement("span");
    size.className = "size";
    size.textContent = file.size + " byte";
    header.appendChild(name);
    header.appendChild(size);
    details.appendChild(header);

    let progress = document.createElement("div");
    progress.className = "progress";
    let bar = document.createElement("div");
    bar.className = "bar";
    progress.appendChild(bar);
    details.appendChild(progress);

    let status = document.createElement("div");
    status.className = "status";
    let percent = document.createElement("span");
    percent.className = "percent";
    percent.textContent = "100%";
    let speed = document.createElement("span");
    speed.className = "speed";
    speed.textContent = "Complete";
    status.appendChild(percent);
    status.appendChild(speed);
    details.appendChild(status);

    fileDOM.appendChild(details);

    return fileDOM;
  }

  dropArea.addEventListener("dragenter", highlight, false);
  dropArea.addEventListener("dragover", highlight, false);
  dropArea.addEventListener("dragleave", unhighlight, false);
  dropArea.addEventListener("drop", handleDrop, false);

  return {
    handleFiles
  };
}
