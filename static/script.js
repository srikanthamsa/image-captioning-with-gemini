function previewFile() {
  const preview = document.getElementById("image-preview");
  const file = document.querySelector("input[type=file]").files[0];
  const reader = new FileReader();

  reader.addEventListener(
    "load",
    function () {
      // Convert image file to base64 string and display it
      preview.src = reader.result;
      document.getElementById("image-preview-container").style.display =
        "block";
    },
    false
  );

  if (file) {
    reader.readAsDataURL(file);
  }
}

function handleForm(event) {
  event.preventDefault();
  const formData = new FormData(event.target);
  fetch("/upload", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      const tagsContainer = document.getElementById("tags");
      tagsContainer.innerHTML = ""; // Clear previous tags
      data.tags.forEach((tag) => {
        const tagElement = document.createElement("div");
        tagElement.textContent = tag;
        tagElement.className = "tag";
        tagsContainer.appendChild(tagElement);
      });
      tagsContainer.style.display = "block"; // Show the tags card
    })
    .catch((error) => console.error("Error:", error));
}
