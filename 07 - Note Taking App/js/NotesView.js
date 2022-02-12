export default class NotesView {
    constructor(root,{onNoteSelect, onNoteAdd, onNoteEdit, onNoteDelete} = {}) {
        this.root = root
        this.onNoteSelect = onNoteSelect
        this.onNoteAdd = onNoteAdd
        this.onNoteEdit = onNoteEdit
        this.onNoteDelete = onNoteDelete
        this.root.innerHTML = 
        `
            <div class="notes__sidebar">
                <button class="notes__add" type="button">Add Note</button>
                <div class="notes__list"></div>
            </div>
            <div class="notes__preview">
                <input class="notes__title" type="text" placeholder="New Note...">
                <textarea class="notes__body">Take Note...</textarea>
            </div>
        `
        this.btnAddNote = this.root.querySelector(".notes__add")
        this.inpTitle = this.root.querySelector(".notes__title")
        this.inpBody = this.root.querySelector(".notes__body")
 
        this.btnAddNote.addEventListener('click',() => [
            onNoteAdd()
        ]
        )
        
        this.inpBody.addEventListener('blur', () => {
            const inpTitle = this.inpTitle.value.trim(); 
            const inpBody = this.inpBody.value.trim()
    
            this.onNoteEdit(inpTitle, inpBody) 
        })       
        this.inpTitle.addEventListener('blur', () => {
            const inpTitle = this.inpTitle.value.trim(); 
            const inpBody = this.inpBody.value.trim()
    
            this.onNoteEdit(inpTitle, inpBody) 
        })

        // Hide preview notes by default
        this.updateNotePreviewVisibility(false)
    }

    _createListItemHTML(id, title, body, updated) {
        const MAX_LENGTH = 60

        return `
            <div class="notes__list-item" data-note-id= "${id}">
                <div class="notes__small-title">${title}</div>
                <div class="notes__small-body">
                    ${body.substring(0,MAX_LENGTH)}
                    ${body.length > MAX_LENGTH ? '...' : ''}
                </div>
                <div class="notes__small-updated">
                    ${updated.toLocaleString(undefined, { dateStyle: "full", timeStyle: "short" })}
                </div>
            </div>
        `
    }

    updateNoteList(notes) {
        const noteListContainer = this.root.querySelector('.notes__list')

        // Empty The List
        noteListContainer.innerHTML = ""

        for (const note of notes) {
            const noteHTML = this._createListItemHTML(note.id,note.title,note.body,new Date(note.updated))

            noteListContainer.insertAdjacentHTML("beforeend", noteHTML)
        }

        // Add Select/Delete Events for each note
        noteListContainer.querySelectorAll('.notes__list-item').forEach(
            listItem => {
                listItem.addEventListener('click', () => {
                    this.onNoteSelect(listItem.dataset.noteId)
                })
                listItem.addEventListener('dblclick', () => {
                    const doAgree = confirm("Are you sure you want to delete this note")
                    if (doAgree) {
                        this.onNoteDelete(listItem.dataset.noteId)
                    }
                })
            }
        );
    }

    updateActiveNote(note) {
        this.root.querySelector('.notes__title').value = note.title
        this.root.querySelector('.notes__body').value = note.body

        this.root.querySelectorAll('.notes__list-item').forEach( (noteListItem) => {
            noteListItem.classList.remove('notes__list-item--selected');
        })

        this.root.querySelector(`.notes__list-item[data-note-id="${note.id}"]`).classList.add('notes__list-item--selected')
    }

    updateNotePreviewVisibility(visibility) {
        this.root.querySelector('.notes__preview').style.visibility = visibility ? "visible" : "hidden"
    }
}