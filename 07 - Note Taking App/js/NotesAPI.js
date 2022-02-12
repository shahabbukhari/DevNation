export default class NotesAPI {
    static getAllNotes() {
        const notes = JSON.parse(localStorage.getItem("allNotes" || []))
        notes.sort( (a,b) => new Date(a.updated) > new Date(b.updated) ? -1 : 1)
        return notes
    }

    static saveNote(noteToAdd) {
        // Add/Update
        const notes = this.getAllNotes()
        const existing =  notes.find( note => note.id === noteToAdd.id)

        if (existing) {
            existing.body = noteToAdd.body
            existing.title = noteToAdd.title
            existing.updated = new Date().toISOString()
        } else {
            noteToAdd.id = Math.floor(Math.random() * 1000000)
            noteToAdd.updated = new Date().toISOString()
            notes.push(noteToAdd)
        }
        localStorage.setItem('allNotes', JSON.stringify(notes))
    }

    static deleteNote(id) {
        const notes = this.getAllNotes()
        const newNotes = notes.filter( note => note.id != id )

        localStorage.setItem('allNotes', JSON.stringify(newNotes))
    }
}