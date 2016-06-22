from flask import render_template

class Races():
    @staticmethod
    def get_races():
        races = [
            {"raceName": "race1"},
            {"raceName": "race2"}
        ]

        return races
