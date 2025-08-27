"""Directory Agent: Shows directory structure and file listings."""
from agent_plugin import AgentPlugin
from rich.prompt import Prompt
from rich.tree import Tree
from rich.table import Table
import os
import stat
from datetime import datetime

class DirectoryAgent(AgentPlugin):
    def __init__(self, model, **kwargs):
        super().__init__(model, **kwargs)

    def run_agent_flow(self, context, **kwargs):
        self.console.print("[bold green]Directory Agent activated![/bold green]")
        
        current_dir = os.getcwd()
        self.console.print(f"[cyan]Current Directory: {current_dir}[/cyan]")
        
        action = Prompt.ask(
            "[bold green]What would you like to do?[/bold green]",
            choices=["list_files", "tree_view", "dir_info"],
            default="list_files"
        )
        
        if action == "list_files":
            target_dir = Prompt.ask("[bold green]Directory path (Enter for current)[/bold green]", default=current_dir)
            self._list_files(target_dir)
        elif action == "tree_view":
            target_dir = Prompt.ask("[bold green]Directory path (Enter for current)[/bold green]", default=current_dir)
            self._show_tree(target_dir, 2)
        elif action == "dir_info":
            target_dir = Prompt.ask("[bold green]Directory path (Enter for current)[/bold green]", default=current_dir)
            self._directory_info(target_dir)
        
        self.console.print("[dim]Directory agent completed.[/dim]")
    
    def _list_files(self, directory):
        try:
            table = Table(title=f"Files in {directory}")
            table.add_column("Name", style="cyan")
            table.add_column("Type", style="magenta") 
            table.add_column("Size", style="green")
            
            for item in sorted(os.listdir(directory)):
                item_path = os.path.join(directory, item)
                is_dir = os.path.isdir(item_path)
                if is_dir:
                    size = "<DIR>"
                    item_type = "Directory"
                else:
                    try:
                        size = f"{os.path.getsize(item_path)} bytes"
                    except:
                        size = "Error"
                    item_type = "File"
                table.add_row(item, item_type, size)
            
            self.console.print(table)
        except Exception as e:
            self.console.print(f"[red]Error: {e}[/red]")
    
    def _show_tree(self, directory, max_depth):
        try:
            tree = Tree(f" {directory}")
            self._build_tree(tree, directory, max_depth, 0)
            self.console.print(tree)
        except Exception as e:
            self.console.print(f"[red]Error: {e}[/red]")
    
    def _build_tree(self, tree, directory, max_depth, current_depth):
        if current_depth >= max_depth:
            return
        try:
            for item in sorted(os.listdir(directory)):
                item_path = os.path.join(directory, item)
                if os.path.isdir(item_path):
                    branch = tree.add(f" {item}")
                    self._build_tree(branch, item_path, max_depth, current_depth + 1)
                else:
                    tree.add(f" {item}")
        except:
            tree.add(" Permission denied")
    
    def _directory_info(self, directory):
        try:
            file_count = 0
            dir_count = 0
            
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                if os.path.isdir(item_path):
                    dir_count += 1
                else:
                    file_count += 1
            
            self.console.print(f"[cyan]Directory: {directory}[/cyan]")
            self.console.print(f"[cyan]Files: {file_count}[/cyan]") 
            self.console.print(f"[cyan]Subdirectories: {dir_count}[/cyan]")
        except Exception as e:
            self.console.print(f"[red]Error: {e}[/red]")
