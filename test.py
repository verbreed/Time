import pygame
import asyncio

async def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((255, 0, 0))  # Just red screen
        pygame.display.flip()
        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())