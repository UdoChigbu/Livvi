const file_input = document.getElementById("file_input");
const file_status = document.getElementById("file_status");
const file_modal = document.getElementById("file_modal");
const cancel_btn = document.getElementById("cancel_btn");

file_input.addEventListener("change", () => {
    if (file_input.files.length>0){
        const file = file_input.files[0];
        const file_size=file.size;
        const file_name = file.name;
        file_status.textContent= `${file_name} (${(file_size/1024).toFixed(1)} KB)`;
        file_modal.style.display = "flex";
    }

});

cancel_btn.addEventListener("click", ()=>{
    file_modal.style.display = "none";
});