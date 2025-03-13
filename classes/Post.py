import pygame

from constants import *
from helpers import screen


class Post:
    """
    A class used to represent post on Nitzagram
    """

    def __init__(self, username, location, description):
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = 0
        self.comments = []
        self.comments_display_index = 0

    def add_like(self):
        self.likes_counter += 1

    def add_comment(self, text):
        comment = comments.append(text)
        self.comments.append(comment)

    def display(self):
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        text = font.render(self.username, True, BLACK)
        screen.blit(text, [USER_NAME_X_POS, USER_NAME_Y_POS])

        text = font.render(self.description, True, BLACK)
        screen.blit(text, [DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS])

        likes_text = f"Liked by {self.likes_counter} users"
        text = font.render(likes_text, True, BLACK)
        screen.blit(text, [LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS])

        text = font.render(self.location, True, BLACK)
        screen.blit(text, [LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS])

        self.display_comments()

    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break

        class TextPost(Post):
            def __init__(self, username, location, description, text, text_color, background_color):
                super().__init__(username, location, description)
                self.text = text
                self.text_color = text_color
                self.background_color = background_color

            def display(self, screen):






class ImagePost(Post):
        def __Init__(self,username,location,description,image_post):
            super().__init__(username,location,description)
            self.image=pygame.image.load(image_path)
            self.image=pygame.transform.scale(self.image,(POST_WIDTH,POST_HEIGHT))


        def display(self):
            screen.blit(self.image,(POST_X_POS,POST_Y_POS))
            super().display()