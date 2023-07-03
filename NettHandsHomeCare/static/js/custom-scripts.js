 /*------------------
        Profile Editabiity Toggle
    -------*/
    const editProfileButton = document.getElementById("edit-button")
    const cancelChangesButton = document.getElementById("cancel-edits-btn")

    function makeProfileEdits(){
        const editableFields = document.querySelectorAll('.editable')
        editableFields.forEach((field) => {
            field.removeAttribute('readonly')
        })
        const saveChangeButton = document.getElementById("save-changes-btn")
        saveChangeButton.removeAttribute('hidden')
        cancelChangesButton.removeAttribute('hidden')
        editProfileButton.hidden = true
    }

    function cancelPendingEdits(){
        const employeeProfile = document.getElementById("employee-profile")
        employeeProfile.reset()

    }
cancelChangesButton.addEventListener('click', cancelPendingEdits )
editProfileButton.addEventListener('click', makeProfileEdits )
