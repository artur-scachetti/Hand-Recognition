class DragRect():

    def __init__(self, posCenter, size=[150, 150]):
        
        self.piece = 'O'
        self.posCenter = posCenter
        self.size = size
        self.color = (255,0,255)
        
        self.isLocked = False

    def update(self, cursor, is_grabbing):

        cx, cy = self.posCenter
        w, h = self.size

        if cx - w //2 < cursor[0] < cx + w //2 and \
           cy - h //2 < cursor[1] < cy + h //2:
            
            if is_grabbing:
                self.posCenter = cursor
                self.color = (0, 255, 0)
                return True
            
            else:
                self.color = (255, 100, 255)

        else:
            self.color = (255, 0, 255)

        return False
    
class Lpiece(DragRect):

    def __init__(self, posCenter, size=[225, 225]):
        super().__init__(posCenter, size)
        self.piece = 'L'

    def update(self, cursor, is_grabbing):

        cx, cy = self.posCenter
        w, h = self.size

        if cx - w //2 < cursor[0] < cx - w //6 and \
           cy - h //2 < cursor[1] < cy + h //2 or \
           cx - w //2 < cursor[0] < cx + w //6 and \
           cy + h //6 < cursor[1] < cy + h //2:
            
            if is_grabbing:
                self.posCenter = cursor
                self.color = (0, 255, 0)
                return True
            
            else:
                self.color = (255, 100, 255)

        else:
            self.color = (255, 0, 255)

        return False

class Spiece(DragRect):

    def __init__(self, posCenter, size=[225, 225]):
        super().__init__(posCenter, size)
        self.piece = 'S'

    def update(self, cursor, is_grabbing):

        cx, cy = self.posCenter
        w, h = self.size

        if cx - w //6 < cursor[0] < cx + w //2 and \
           cy - h //6 < cursor[1] < cy + h //6 or \
           cx - w //2 < cursor[0] < cx + w //6 and \
           cy + h //6 < cursor[1] < cy + h //2 or \
           cx - w //6 < cursor[0] < cx + w //6 and \
           cy - h //6 < cursor[1] < cy + h //2:
            
            if is_grabbing:
                self.posCenter = cursor
                self.color = (0, 255, 0)
                return True
            
            else:
                self.color = (255, 100, 255)

        else:
            self.color = (255, 0, 255)

        return False

class Jpiece(DragRect):

    def __init__(self, posCenter, size=[225, 225]):
        super().__init__(posCenter, size)
        self.piece = 'J'

    def update(self, cursor, is_grabbing):

        cx, cy = self.posCenter
        w, h = self.size

        if cx - w //2 < cursor[0] < cx + w //6 and \
           cy - h //2 < cursor[1] < cy - h //6 or \
           cx - w //2 < cursor[0] < cx - w //6 and \
           cy - h //6 < cursor[1] < cy + h //2:
            
            if is_grabbing:
                self.posCenter = cursor
                self.color = (0, 255, 0)
                return True
            
            else:
                self.color = (255, 100, 255)

        else:
            self.color = (255, 0, 255)

        return False   
    
class Zpiece(DragRect):

    def __init__(self, posCenter, size=[225, 225]):
        super().__init__(posCenter, size)
        self.piece = 'Z'

    def update(self, cursor, is_grabbing):

        cx, cy = self.posCenter
        w, h = self.size

        if cx - w //2 < cursor[0] < cx + w //6 and \
           cy - h //6 < cursor[1] < cy + h //6 or \
           cx - w //6 < cursor[0] < cx + w //2 and \
           cy + h //6 < cursor[1] < cy + h //2 or \
           cx - w //6 < cursor[0] < cx + w //6 and \
           cy - h //6 < cursor[1] < cy + h //2:
            
            if is_grabbing:
                self.posCenter = cursor
                self.color = (0, 255, 0)
                return True
            
            else:
                self.color = (255, 100, 255)

        else:
            self.color = (255, 0, 255)

        return False

class Tpiece(DragRect):

    def __init__(self, posCenter, size=[225, 225]):
        super().__init__(posCenter, size)
        self.piece = 'T'

    def update(self, cursor, is_grabbing):

        cx, cy = self.posCenter
        w, h = self.size

        if cx - w //6 < cursor[0] < cx + w //6 and \
           cy - h //6 < cursor[1] < cy + h //2 or \
           cx - w //2 < cursor[0] < cx + w //2 and \
           cy + h //6 < cursor[1] < cy + h //2:
            
            if is_grabbing:
                self.posCenter = cursor
                self.color = (0, 255, 0)
                return True
            
            else:
                self.color = (255, 100, 255)

        else:
            self.color = (255, 0, 255)

        return False

class Linepiece(DragRect):

    def __init__(self, posCenter, size=[300, 75]):
        super().__init__(posCenter, size)
        self.piece = 'Line'

    def update(self, cursor, is_grabbing):

        cx, cy = self.posCenter
        w, h = self.size

        if cx - w //2 < cursor[0] < cx + w //2 and \
           cy - h //2 < cursor[1] < cy + h //2:
            
            if is_grabbing:
                self.posCenter = cursor
                self.color = (0, 255, 0)
                return True
            
            else:
                self.color = (255, 100, 255)

        else:
            self.color = (255, 0, 255)

        return False
