import pygame  # pygame 모듈의 임포트
import sys  # 외장 모듈
from pygame.locals import *  # QUIT 등의 pygame 상수들을 로드한다.

width = 1000  # 상수 설정
height = 780
white = (255, 255, 255)
black = (0, 0, 0)
fps = 30
pygame.init()  # 초기화

pygame.display.set_caption('Hello, world!')  # 창 제목 설정
screen = pygame.display.set_mode((width, height))  # 메인 디스플레이를 설정한다
clock = pygame.time.Clock()  # 시간 설정
ship = pygame.image.load("C:\\Users\\PC\\Desktop\\딩코딩코\\파파파팦이이잉썬\\다운로드.jpg")


while True:
    pygame.display.update()
    screen.fill(white)# 화면을 업데이트한다
    # 아래의 코드를 무한 반복한다.
    screen.blit(ship, (0, 0))

    for event in pygame.event.get():  # 발생한 입력 event 목록의 event마다 검사
        if event.type == QUIT:  # event의 type이 QUIT에 해당할 경우
            pygame.quit()  # pygame을 종료한다
            sys.exit()  # 창을 닫는다
      # displaysurf를 하얀색으로 채운다

    pygame.display.update()  # 화면을 업데이트한다
    clock.tick(fps)  # 화면 표시 회수 설정만큼 루프의 간격을 둔다