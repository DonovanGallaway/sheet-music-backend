"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
    RouteGroup([
        Get('/', 'SheetController@index').name('index'),
        Get('/@id', 'SheetController@show').name('show'),
        Post('/', 'SheetController@create').name('create'),
        Put('/@id', "SheetController@update").name('update'),
        Delete('/@id', "SheetController@destroy").name('destory')    
    ], prefix='/music', name='sheets')
]
