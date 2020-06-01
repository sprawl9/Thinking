import pygame, random
####################################################################
# 캐릭터 화면 가장 아래 좌우 이동만 가능, 똥은 화면 가장위에서 떨어지고 x좌표는 랜덤
# 캐락터 똥피하면 다음똥 다시 떨어짐, 캐릭터 똥과 충돌하면 게임종료 , FPS는 30으로 고정

# 기본 초기화 (반드시 해야하는 것들)
pygame.init()   # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("하늘에서 떨어지는 갓 피하기 게임")

# FPS
clock = pygame.time.Clock()
#####################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도, 폰트 등)
background = pygame.image.load("C:\\Users\\spraw\\OneDrive\\바탕 화면\\pythonOne\\pygame_basic\\background.png")
character = pygame.image.load("C:\\Users\\spraw\\OneDrive\\바탕 화면\\pythonOne\\pygame_basic\\kakaocc.jpg")
enemy = pygame.image.load("C:\\Users\\spraw\\OneDrive\\바탕 화면\\pythonOne\\pygame_basic\\hyun.png")
enemy2 = pygame.image.load("C:\\Users\\spraw\\OneDrive\\바탕 화면\\pythonOne\\pygame_basic\\ddong.png")

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height

enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0

enemy2_size = enemy2.get_rect().size
enemy2_width = enemy2_size[0]
enemy2_height = enemy2_size[1]
enemy2_x_pos = random.randint(0, screen_width - enemy2_width)
enemy2_y_pos = 0

to_x = 0
to_y = 0

character_speed = 1.7
enemy_speed = 17
enemy2_speed = 15

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성 (폰트, 크기)

game_result = "Game Nukka Hesseo ?!!!"

# 회피 횟수
evanum = 0

# 총 시간
total_time = 5

# 시작 시간
start_ticks = pygame.time.get_ticks()  # 현재 tick을 받아줌

running = True
while running:
    dt = clock.tick(30)  # 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행중이 아님

    # 3. 게임 캐릭터 위치 정의
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_DOWN:
                to_y += 0
            elif event.key == pygame.K_UP:
                to_y -= 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    if character_y_pos < 0:
        characer_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        characer_y_pos = screen_height - character_height

    enemy_y_pos += enemy_speed
    enemy2_y_pos += enemy2_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)
        evanum += 1
    if enemy2_y_pos > screen_height:
        enemy2_y_pos = 0
        enemy2_x_pos = random.randint(0, screen_width - enemy2_width)    
        evanum += 1

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    enemy2_rect = enemy2.get_rect()
    enemy2_rect.left = enemy2_x_pos
    enemy2_rect.top = enemy2_y_pos

    if character_rect.colliderect(enemy_rect):
        print("망했어요")
        running = False

    if character_rect.colliderect(enemy2_rect):
        print("망했어요")
        running = False        

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(enemy2, (enemy2_x_pos, enemy2_y_pos))

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 경과 시간(밀리세컨드)을 1000으로 나누어서 초(s) 단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    # 출력할 글자, True, 글자 색상
    screen.blit(timer, (10, 10))

    evastr = "GOD SCORE : " + str(evanum)
    eva = game_font.render(evastr, True, (255, 255, 255))
    screen.blit(eva, (210, 10))

    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        game_result = "Godkeun Myun-Jae"
        running = False

    pygame.display.update()  # 게임화면을 다시 그리기
# 겜오버 메시지
msg = game_font.render(game_result, True, (255, 255, 0))  # 노란색
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()
pygame.time.delay(5000)

# pygame 종료
pygame.quit()