class GridWorld:
    def __init__(self, size, start, exit, blocks=None):
        self.size=size
        self.blocks = set() if blocks is None else blocks
        assert not self.danger(exit)
        assert not self.danger(start)
        self.start_pos = start
        self.exit_pos = exit
        self.restart()
        self.V = None
        self.A = None
        
    def restart(self):
        self.score = 0  # +1 win, -1 lose, 0 playing
        self.pos = self.start_pos 
        self.last_move = 0
    
    def is_end(self):
        return self.score != 0
        
    def danger(self, pos):        
        if pos[0]<0 or pos[1]<0:
            return True
        if pos[0]>=self.size[0] or pos[1]>=self.size[1]:
            return True
        return pos in self.blocks
    
    def next_pos(self, d):
        return (self.pos[0]+abs(d-1)-1, self.pos[1]+abs(d-2)-1)
    
    def move(self, d):
        if self.score:
            return self
        self.last_move = d
        # 0 right, 1 up, 2 left, 3 down
        self.pos = self.next_pos(d)
        if self.danger(self.pos):
            self.score = -1
        if self.pos == self.exit_pos:
            self.score = 1
        return self
    
    def _repr_html_(self):
        td_style = "width: 2em;height: 2em;"
        def img(f, style=""):
            style = "style='width: 1.5em;height: 1.5em;{}'".format(style)
            return "<img src='img/{}.png' {}/>".format(f, style)
        s = "<table border=1>"
        for i in range(-1,self.size[0]+1):
            s+="<tr>"            
            for j in range(-1,self.size[1]+1):
                color='#888'
                content = ""
                if self.V is not None:
                    if self.V[i,j] == 2:
                        color="#77f"
                    else:
                        l = min(max(int(self.V[i,j]*128+128),0), 255)
                        color = "#%02x%02x80"%(255-l,l)

                if self.danger((i,j)):                    
                    if (i,j) in self.blocks:
                        content = img('skull')
                    else:
                        content = img('radiation')
                if self.exit_pos == (i,j):                    
                    content = img('cherry')
                if self.pos == (i,j):
                    style = ""
                    imgfn = ['pacman', 'smile', 'frown'][self.score]
                    if self.score == 0:
                        style = "transform: rotate({}deg)".format(-90*self.last_move)
                    content = img(imgfn, style)
                if not content and self.A is not None and self.A[i,j]>=0:
                    style = "transform: rotate({}deg)".format(-90*self.A[i,j])
                    content = img('arrow', style=style)
                    
                s+="<td style='{}background: {}'>".format(td_style,
                                                               color)
                s += content
                    
                s+="</td>"
            s+="</tr>"
        s += "</table>"        
        return s 
        
    