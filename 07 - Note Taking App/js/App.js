import NotesApi from "./NotesApi.js"
import NotesView from "./NotesView.js"

export default class App {
    constructor(root) {
        this.notes = []
        this.activeNotes = null
        this.view = new NotesView(root,this._handlers())

        this._refreshNotes()        
    }

    _refreshNotes() {
        const notes = NotesApi.getAllNotes()

        this._setNotes(notes)

        if (notes.length > 0) {
            this._setActiveNotes(notes[0])
        }
    }

    _setNotes(notes) {
        this.notes = notes
        this.view.updateNoteList(notes)
        this.view.updateNotePreviewVisibility(notes.length > 0)
    }

    _setActiveNotes(note) {
        this.activeNotes = note
        this.view.updateActiveNote(note)
    }

    _handlers() {
        
        return {
            onNoteAdd: () => {
                const newNode = {
                    body: "Take New Note...",
                    title: "New Note"
                }
                NotesApi.saveNote(newNode)
                this._refreshNotes()
            },
            onNoteEdit: (title,body) => {
                const edited = {
                    body: body,
                    title: title,
                    id: this.activeNotes.id
                }
                NotesApi.saveNote(edited)
                // this._handlers
                this._refreshNotes()
            },
            onNoteSelect: (noteId) => {
                const selectedNote = this.notes.find( note => note.id == noteId )
                this._setActiveNotes(selectedNote)
            },
            onNoteDelete: (id) => {
                NotesApi.deleteNote(id)
                this._refreshNotes()
            }
        }
    }
}