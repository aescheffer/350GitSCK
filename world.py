#first level world creation class
class World():
    def __init__(self,data):
        self.tile_list = []

        #load images
        dirt_img = pygame.image.load('img/stone.jpg')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                #based on the tile number, place a certain image/enemy into that location on the board
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size,tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    exit = Exit(col_count * tile_size, row_count * tile_size - (tile_size//2))
                    exit_group.add(exit)
                if tile == 4:
                    dragon = Dragon(col_count * tile_size, row_count * tile_size)
                    dragon_group.add(dragon)
                col_count += 1
            row_count += 1

    #draw the world onto the screen
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0],tile[1])



#second level world creation
class World2():
    def __init__(self, data):
        self.tileList = []

        #load image
        wall_img = pygame.image.load('img/underwaterWalls.jpg')

        rcount = 0
        for row in data:
            ccount = 0
            for tile in row:
                #places images in certain positions depending on numbers on the world board
                if tile == 1:
                    img = pygame.transform.scale(wall_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = ccount * tile_size
                    img_rect.y = rcount * tile_size
                    self.tileList.append((img, img_rect))
                if tile == 2:
                    mermaid = Mermaids1(ccount * tile_size, rcount * tile_size)
                    mermaid_group.add(mermaid)
                if tile == 3:
                    mermaid = Mermaids2(ccount * tile_size, rcount * tile_size)
                    mermaid_group.add(mermaid)
                if tile == 4:
                    mermaid = Mermaids3(ccount * tile_size+10, rcount * tile_size)
                    mermaid_group.add(mermaid)
                if tile == 5:
                    egg = Exit(ccount * tile_size, rcount * tile_size - (tile_size // 2))
                    exit_group2.add(egg)


                ccount += 1
            rcount += 1

    #draws world on screen
    def draw(self):
        for tile in self.tileList:
            screen.blit(tile[0], tile[1])


#third and final world creation
class World3():
    def __init__(self, data):
        self.tile_list = []
        #load images
        dirt_img = pygame.image.load('img/hedges.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                #create and place dirt and enemies
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    bad = Enemy2(col_count * tile_size, row_count * tile_size, 'img/viktorkrum.png', (80,90), 'horiz')
                    bad_group.add(bad)
                if tile == 3:
                    exit = Exit(col_count * tile_size, row_count * tile_size - (tile_size//2))
                    exit_group3.add(exit)
                if tile == 4:
                    bad = Enemy2(col_count * tile_size, row_count * tile_size, 'img/vines.png', (50, 70), 'vert')
                    bad_group.add(bad)

                if tile == 5:
                    bad = Enemy2(col_count * tile_size, row_count * tile_size, 'img/spider.png', (50, 70), 'vertigo')
                    bad_group.add(bad)
                col_count += 1
            row_count += 1

    #draw world onto the screen
    def draw(self):
        for tile in self.tile_list:
            #takes picture and puts it in the location of rect coordinates
            screen.blit(tile[0], tile[1])

class Exit(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/trophy.png')
        self.image = pygame.transform.scale(img, (tile_size, int(tile_size*1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


#first screen the user sees--gives instructions on what to expect
#when space bar is pressed, user starts first level
#when restart is called, this class will allow user to return to opening screen
class Start:
    def __init__(self):
        pass

    #updates game over variable depending on if space bar is pressed by user
    def update(self, game_over):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            game_over = 1

        return game_over