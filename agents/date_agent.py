"""Date Agent: Provides current date and date calculations."""
from agent_plugin import AgentPlugin
from rich.prompt import Prompt
from datetime import datetime, timedelta
import calendar

class DateAgent(AgentPlugin):
    def __init__(self, model, **kwargs):
        super().__init__(model, **kwargs)

    def run_agent_flow(self, context, **kwargs):
        """Run the date agent - provides date information and calculations."""
        self.console.print("[bold green]Date Agent activated![/bold green]")
        
        now = datetime.now()
        
        # Display current date information
        self.console.print(f"[cyan]Today's Date: {now.strftime('%Y-%m-%d')}[/cyan]")
        self.console.print(f"[cyan]Full Date: {now.strftime('%A, %B %d, %Y')}[/cyan]")
        self.console.print(f"[cyan]Day of Year: {now.timetuple().tm_yday}[/cyan]")
        self.console.print(f"[cyan]Days Until New Year: {(datetime(now.year + 1, 1, 1) - now).days}[/cyan]")
        
        # Check if it's a leap year
        is_leap = calendar.isleap(now.year)
        self.console.print(f"[cyan]Leap Year: {'Yes' if is_leap else 'No'}[/cyan]")
        
        # Show month calendar
        self.console.print(f"\n[bold yellow]Calendar for {now.strftime('%B %Y')}:[/bold yellow]")
        cal = calendar.month(now.year, now.month)
        self.console.print(f"[dim]{cal}[/dim]")
        
        # Ask for date calculations
        calc_choice = Prompt.ask(
            "[bold green]What would you like to calculate?[/bold green]",
            choices=["days_between", "add_days", "subtract_days", "age", "none"],
            default="none"
        )
        
        if calc_choice == "days_between":
            date1_str = Prompt.ask("[bold green]Enter first date (YYYY-MM-DD)[/bold green]")
            date2_str = Prompt.ask("[bold green]Enter second date (YYYY-MM-DD)[/bold green]")
            try:
                date1 = datetime.strptime(date1_str, '%Y-%m-%d')
                date2 = datetime.strptime(date2_str, '%Y-%m-%d')
                diff = abs((date2 - date1).days)
                self.console.print(f"[cyan]Days between {date1_str} and {date2_str}: {diff} days[/cyan]")
            except ValueError:
                self.console.print("[red]Invalid date format. Please use YYYY-MM-DD[/red]")
        
        elif calc_choice == "add_days":
            days_to_add = int(Prompt.ask("[bold green]How many days to add to today?[/bold green]"))
            future_date = now + timedelta(days=days_to_add)
            self.console.print(f"[cyan]Date after adding {days_to_add} days: {future_date.strftime('%Y-%m-%d (%A)')}[/cyan]")
        
        elif calc_choice == "subtract_days":
            days_to_subtract = int(Prompt.ask("[bold green]How many days to subtract from today?[/bold green]"))
            past_date = now - timedelta(days=days_to_subtract)
            self.console.print(f"[cyan]Date after subtracting {days_to_subtract} days: {past_date.strftime('%Y-%m-%d (%A)')}[/cyan]")
        
        elif calc_choice == "age":
            birth_date_str = Prompt.ask("[bold green]Enter your birth date (YYYY-MM-DD)[/bold green]")
            try:
                birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d')
                age_days = (now - birth_date).days
                age_years = age_days // 365.25
                self.console.print(f"[cyan]You are approximately {age_years:.1f} years old ({age_days} days)[/cyan]")
            except ValueError:
                self.console.print("[red]Invalid date format. Please use YYYY-MM-DD[/red]")
        
        self.console.print("[dim]Date agent completed.[/dim]")
