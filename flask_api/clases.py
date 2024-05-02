class Estilo:
    def __init__(self, titulo, descripcion, subestilos):
        self.descripcion = descripcion
        self.titulo = titulo
        self.subestilos = subestilos

    def to_dict(self):
        return {
            'titulo': self.titulo,
            'descripcion': self.descripcion,
            'subestilos': [subestilo.to_dict() for subestilo in self.subestilos] if self.subestilos else None
        }

class Subestilo:
    def __init__(self, titulo, descripcion, aspecto, cuerpo, aroma, sabor, alcohol, subestilos):
        self.titulo = titulo
        self.descripcion = descripcion
        self.aspecto = aspecto
        self.cuerpo = cuerpo
        self.aroma = aroma
        self.sabor = sabor
        self.alcohol = alcohol
        self.subestilos = subestilos

    def to_dict(self):         
        
        return {
            'titulo': self.titulo,
            'descripcion': self.descripcion,
            'aspecto': self.aspecto,
            'cuerpo': self.cuerpo,
            'aroma': self.aroma,
            'sabor': self.sabor,
            'alcohol': self.alcohol,
            'subestilos': [subestilo.to_dict() for subestilo in self.subestilos] if self.subestilos else None
        }