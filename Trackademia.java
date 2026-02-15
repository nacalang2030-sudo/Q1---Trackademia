import java.util.*;

public class Trackademia {
    private static Map<String, Double> grades = new HashMap<>();
    private static List<String[]> assignments = new ArrayList<>();
    private static Map<String, String> schedules = new HashMap<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Welcome to Trackademia!");
        
        while (true) {
            displayMenu();
            String choice = scanner.nextLine();
            
            switch (choice) {
                case "1":
                    addGrade(scanner);
                    break;
                case "2":
                    viewGrades();
                    break;
                case "3":
                    addAssignment(scanner);
                    break;
                case "4":
                    viewAssignments();
                    break;
                case "5":
                    addSchedule(scanner);
                    break;
                case "6":
                    viewSchedules();
                    break;
                case "0":
                    System.out.println("====  HAVE A NICE DAY!  ====");
                    System.out.println("Thank you for using Trackademia!");
                    scanner.close();
                    return;
                default:
                    System.out.println("====  HAVE A NICE DAY!  ====");
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }
    
    private static void displayMenu() {
        System.out.println("\nMenu:");
        System.out.println("1 - Add Grade");
        System.out.println("2 - View Grades");
        System.out.println("3 - Add Assignment");
        System.out.println("4 - View Assignments");
        System.out.println("5 - Add Class Schedule");
        System.out.println("6 - View Schedules");
        System.out.println("0 - Exit");
        System.out.println("===============");
        System.out.print("Enter your choice: ");
    }
    
    private static void addGrade(Scanner scanner) {
        System.out.print("Enter the name of the subject: ");
        String subject = scanner.nextLine();
        System.out.print("Enter grade: ");
        try {
            double grade = Double.parseDouble(scanner.nextLine());
            grades.put(subject, grade);
            System.out.println("======  GRADE  ======");
            System.out.println("Grade saved");
        } catch (NumberFormatException e) {
            System.out.println("Invalid grade format. Please enter a number.");
        }
    }
    
    private static void viewGrades() {
        System.out.println("Grades:");
        if (grades.isEmpty()) {
            System.out.println("======  GRADE  ======");
            System.out.println("No grades saved yet :>");
        } else {
            for (Map.Entry<String, Double> entry : grades.entrySet()) {
                System.out.println(entry.getKey() + ": " + entry.getValue());
            }
            double average = grades.values().stream().mapToDouble(Double::doubleValue).average().orElse(0);
            System.out.println("======  GRADE  ======");
            System.out.printf("Average Grade: %.2f\n", average);
        }
    }
    
    private static void addAssignment(Scanner scanner) {
        System.out.print("Enter assignment's name: ");
        String name = scanner.nextLine();
        System.out.print("Enter the deadline: ");
        String deadline = scanner.nextLine();
        assignments.add(new String[]{name, deadline});
        System.out.println("====== ASSIGNMENTS  ======");
        System.out.println("Assignment saved!");
    }
    
    private static void viewAssignments() {
        if (assignments.isEmpty()) {
            System.out.println("====== ASSIGNMENTS  ======");
            System.out.println("No assignments saved yet");
        } else {
            System.out.println("Assignments:");
            for (String[] assignment : assignments) {
                System.out.println("====== ASSIGNMENTS  ======");
                System.out.println(assignment[0] + " - Due: " + assignment[1]);
            }
        }
    }
    
    private static void addSchedule(Scanner scanner) {
        System.out.print("Enter subject name: ");
        String subject = scanner.nextLine();
        System.out.print("Enter schedule (Day & Time): ");
        String schedule = scanner.nextLine();
        schedules.put(subject, schedule);
        System.out.println("======  SCHEDULE  ======");
        System.out.println("Schedule saved!");
    }
    
    private static void viewSchedules() {
        if (schedules.isEmpty()) {
            System.out.println("======  SCHEDULES  ======");
            System.out.println("No schedules saved yet.");
        } else {
            System.out.println("Schedules:");
            for (Map.Entry<String, String> entry : schedules.entrySet()) {
                System.out.println("======  SCHEDULES  ======");
                System.out.println(entry.getKey() + ": " + entry.getValue());
            }
        }
    }
}