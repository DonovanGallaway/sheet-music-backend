""" A SheetController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Sheet import Sheet

class SheetController(Controller):
    """Class Docstring Description
    """
    
    def __init__(self, request:Request):
        self.request = request
    

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", SheetController)
        """
        id = self.request.param('id')
        return Sheet.find(id)
        

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", SheetController)
        """
        return Sheet.all()

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", SheetController)
        """
        name = self.request.input('name')
        instrumentation = self.request.input('instrumentation')
        link = self.request.input('link')
        sheet = Sheet.create({'name':name,'instrumentation':instrumentation,'link':link})
        return sheet

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", SheetController)
        """
        id = self.request.param('id')
        name = self.request.input('name')
        instrumentation = self.request.input('instrumentation')
        link = self.request.input('link')
        Sheet.where('id',id).update({'name':name,'instrumentation':instrumentation,'link':link})
        return Sheet.find(id)

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", SheetController)
        """
        id = self.request.param('id')
        sheet = Sheet.find(id)
        Sheet.where('id',id).delete()
        return sheet