from tkinter import *  # noqa: F403
from typing import Dict
from typing import List

from exekute.core.const import Colors
from exekute.core.const import TASK_EDIT_BTNS
from exekute.core.const import TASK_EDIT_ENTRY_BOX
from exekute.core.db import DataBase
from exekute.core.utils import load_image
from exekute.core.utils import verify_exe_file
from exekute.core.utils import verify_script_file


class EditTask(Frame):

    def __init__(self, parent: Tk, task_id: str, te_cb) -> None:
        super(EditTask, self).__init__(parent, width=1000, height=700)

        self.db = DataBase()
        self._id = task_id
        self.te_cb = te_cb  # task edit call back

        self.data = self.db.get_by_id(task_id)
        self.exe_name_to_path: Dict[str, str] = {}

        self.setup_ui()

    def setup_ui(self) -> None:
        edit_task_bg = load_image("edit-task-window.png")
        save_btn_bg = load_image("save-button.png")
        clear_all_btn_bg = load_image("clear-all-button.png")
        delete_btn_bg = load_image("delete-button.png")
        back_btn_bg = load_image("back-button.png")

        self.entry_boxes: List[Entry] = []

        self.e_task_bg = Label(self, image=edit_task_bg, borderwidth=0)
        self.e_task_bg.image = edit_task_bg
        self.e_task_bg.place(x=0, y=0)

        self.task_name = Entry(self, font=("arial", 39), borderwidth=0,
                               highlightthickness=0, background=Colors.black, fg="white", width=31)
        self.task_name.place(x=39, y=10)

        if not self.data["name"]:
            self.task_name.delete(0, END)
            self.task_name.insert(0, "Group name")

        else:
            self.task_name.delete(0, END)
            self.task_name.insert(0, self.data["name"])

        # add all the five entry box for the app names
        for i in range(1, 6):
            entry = Entry(self, borderwidth=0,
                          highlightthickness=0, font=("arial", 16), width=53, background=Colors.grey)
            self.entry_boxes.append(entry)
            entry.place(**TASK_EDIT_ENTRY_BOX[i])

        # add the entry box for the script
        self.script_entry = Entry(self, borderwidth=0,
                                  highlightthickness=0, font=("arial", 16), width=53, background=Colors.grey)
        self.script_entry.place(**TASK_EDIT_ENTRY_BOX[6])
        self.script_entry.bind("<FocusIn>", self.entry_focus_in)
        self.script_entry.bind("<FocusOut>", self.entry_focus_out)

        # fill the all the app names
        count = 0
        for app in self.data["apps"]:

            exe_name = app.split("\\")[-1]
            self.exe_name_to_path[exe_name] = app

            self.entry_boxes[count].delete(0, END)
            self.entry_boxes[count].insert(0, exe_name)
            self.entry_boxes[count].bind("<FocusIn>", self.entry_focus_in)
            self.entry_boxes[count].bind("<FocusOut>", self.entry_focus_out)
            count += 1

        self.script_entry.delete(0, END)
        script_name = self.data["script"].split("\\")[-1]
        self.script_entry.insert(0, script_name)
        self.exe_name_to_path[script_name] = self.data["script"]

        # add all the buttons
        self.save_btn = Button(self, image=save_btn_bg, background=Colors.black,
                               activebackground=Colors.black, borderwidth=0, command=self.save, cursor="hand2")
        self.save_btn.image = save_btn_bg
        self.clr_btn = Button(self, image=clear_all_btn_bg, background=Colors.black,
                              activebackground=Colors.black, borderwidth=0, command=self.clear_all, cursor="hand2")
        self.clr_btn.image = clear_all_btn_bg
        self.del_btn = Button(self, image=delete_btn_bg, background=Colors.black,
                              activebackground=Colors.black, borderwidth=0, command=self.delete, cursor="hand2")
        self.del_btn.image = delete_btn_bg

        self.back_btn = Button(self, image=back_btn_bg, background=Colors.black,
                               activebackground=Colors.black, borderwidth=0, command=self.back, cursor="hand2")
        self.back_btn.image = back_btn_bg

        self.save_btn.place(**TASK_EDIT_BTNS[1])
        self.clr_btn.place(**TASK_EDIT_BTNS[2])
        self.del_btn.place(**TASK_EDIT_BTNS[3])
        self.back_btn.place(**TASK_EDIT_BTNS[4])

    def entry_focus_in(self, e):
        exe_name = e.widget.get()
        if exe_name:
            e.widget.delete(0, END)
            e.widget.insert(0, self.exe_name_to_path[exe_name])

    def entry_focus_out(self, e):
        link = e.widget.get()

        if link:
            for k, v in self.exe_name_to_path.items():
                if v == link:
                    e.widget.delete(0, END)
                    e.widget.insert(0, k)

    def button_click(self, e):
        print(e)

    def clear_all(self) -> None:
        for eb in self.entry_boxes:
            eb.delete(0, END)
        self.script_entry.delete(0, END)

    def save(self) -> None:
        add = True
        data = {}
        data["name"] = self.task_name.get()
        apps = []
        for tb in self.entry_boxes:
            app = tb.get().rstrip().lstrip()
            if app:
                if app in self.exe_name_to_path:
                    app = self.exe_name_to_path[app]
                if not verify_exe_file(app):
                    print(app)
                    add = False
                    break
                apps.append(app)
        data["apps"] = apps.copy()

        script = self.script_entry.get().lstrip().rstrip()
        if script:
            if script in self.exe_name_to_path:
                script = self.exe_name_to_path[script]
            if verify_script_file(script):
                data["script"] = script

            else:
                print("script")
                add = False
        else:
            data["script"] = ""

        if add:
            self.db.add(self._id, data)
            self.destroy()
            self.te_cb()
        else:
            self.display_error_msg()

    def delete(self) -> None:
        self.db.del_by_id(self._id)
        self.destroy()
        self.te_cb()

    def back(self) -> None:
        if not self.db.get_by_id(self._id)["name"]:

            self.db.del_by_id(self._id)
        self.destroy()
        self.te_cb()

    def display_error_msg(self):
        self.error_label = Label(self, text="Oops!. Some file paths are not valid.", font=(
            "roboto", 12), background=Colors.black, borderwidth=0, fg="red")
        self.error_label.place(x=77, y=664)
        self.after(900, self.error_label.destroy)
