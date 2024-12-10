document.addEventListener("DOMContentLoaded", () => {
    
    // Edit button functionality
    const editButtons = document.getElementsByClassName("btn-edit");
    const commentText = document.getElementById("id_body");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");
  
    if (editButtons && commentText && commentForm && submitButton) {
      for (let button of editButtons) {
        button.addEventListener("click", (e) => {
          let commentId = e.target.getAttribute("comment_id");
          let commentContent = document.getElementById(`comment${commentId}`).innerText;
          commentText.value = commentContent;
          submitButton.innerText = "Update";
          commentForm.setAttribute("action", `edit_comment/${commentId}`);
        });
      }
    }
  
    // Delete button functionality
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteModal = document.getElementById("deleteModal");
    const deleteConfirm = document.getElementById("deleteConfirm");
  
    if (deleteButtons && deleteModal && deleteConfirm) {
      const bootstrapModal = bootstrap.Modal.getOrCreateInstance(deleteModal);
  
      for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
          let commentId = e.target.getAttribute("comment_id");
          deleteConfirm.href = `delete_comment/${commentId}`;
          bootstrapModal.show();
        });
      }
    }
  });
  