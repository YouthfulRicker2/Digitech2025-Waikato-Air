# Waikato Air

## Overview

This is some work for my 2025 NCEA Level 3 Digitech Class at [Wainuiomata High School](https://wainuiomatahigh.school.nz/).

## Main Project (FlightCal)

This is a program designed for use by Travel Agents who wish to provide their customers the cost of a flight through email. The program calculates the cost of the flight using the age of the customer as well as the amount of seats remaining and how close the date of the flight is, and it then provides a simple copy-pastable email for the Agent to send.\
To the best of my ability I have followed pep8 and pep257 styling conventions for the python language to maximize readability and convenience.

### How to Use:

1. Run the [main.py](main.py) file with Python,\
2. Follow the instructions the program gives you until you reach your desired result.

### Requirements

- [x] Generate a flight number for each flight,
- [x] Have a set flight cost per route,
- [x] Ask agent for flight info;
    - [x] Remaining seats,
    - [x] Traveller info;
        - [x] Name,
        - [x] Age,
    - [x] Route,
- [x] Have persistent storage of client data;
    - [x] Read from CSV file,
    - [x] Append to CSV file,
- [x] Calculate a discount (from age, seat scarcity, and flight date),
- [x] Output of a copy-pastable email for the client,

#### Code Requirements

- [x] Read from separate python files,
- [x] Utilize classes,
- [x] Handle input errors and prevent mistakes.

#### Post-Stakeholder

##### Stakeholder 1: Padre
- [x] Specify what type of discount the client is getting.

##### Stakeholder 2: Caleb
- [x] Have a 'mailto:' link open upon request.

### Solution Design

I created a flowchart to pre-configure the structure of my program before I began creating it: [flowchart link](https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000FF&edit=_blank&layers=1&nav=1&title=Program%20Flowchart.drawio&dark=auto#R%3Cmxfile%3E%3Cdiagram%20name%3D%22Page-1%22%20id%3D%22WkENpaIAz4KM4MTKUci-%22%3E7R1bc5u4%2Btd4zu6DPUggLo9J3HY729ukZ9vdpzPExjYttlzASby%2F%2FkiAMEjYKDYgudM%2BNCAQhu9%2B06eRebd%2BfhP729V7PA%2BiETTmzyNzOoIQmtAhf%2BjIPh8BruvmI8s4nBdjh4HP4b9BMWgUo7twHiS1G1OMozTc1gdneLMJZmltzI9j%2FFS%2FbYGj%2Bq9u%2FWUgDHye%2BZE4%2BjWcp6t81EXGYfyPIFyu2C8Do7iy9tnNxUCy8uf4qTJkvhqZdzHGaX60fr4LIgo9Bpd83usjV8sXi4NNKjPB%2BmF881%2FZyy%2F4%2FR8W%2BPYl%2FGC44%2BIpj360Kz74LgrpA6ExDVI%2FjJLi5dM9gwj5ji09nO2jcDMPYnNk3j6twjT4vPVn9MITIQUytkrXETkD5PAB78id83cP5YA%2F%2B76M6ejHXUoeExTjSY5%2FgMix%2BH3sZYM4DZ4rQ8X3vgnwOkjjPbmluDr2GBkV5OeZxfnTAZclxlYVPLrFmF%2BQz7J89gHC5KAA8gsADgWAv46yn%2F05AI4Q0gzgtikANJgTFi9OcZyu8BJv%2FOjVYfQ2zuFHrhvk7HDPO4y3BeS%2BBWm6L%2BSVv0txHQHBc5j%2BXTn%2Bhz5qgoqz6XPx5OxkXzn5FMQh%2Be4gZmMbAoO%2FqyeVJ9HTw6OyM%2Faso7hM8C6eBSfgVYAr9eNlkJ64D9n5jRSYJ0kjDiI%2FDR%2Fr8rR7NDvaoPkokqFTUsD14NnWC8%2BmID9vMf4ebpY%2FiQCFhm4ayxIg%2FsFfB0eBTD7fj6IgwsvYXxOgbCuUXrtWYYE2bCzC54DZhqAr0wDWAW1bDYCGDYC2%2BwI0w7QGImwCW1RVKa6KO0uJ1Zu8QpLyinkc3cmrbOpNHPv7yg1bHG7SpPLkT3SgQl%2B2w9FXoTBfS0%2Fg7Xl%2BgolOTiAH%2BUsfKLL8%2BvOJFAnS4GZ5%2FcLANXQTBo4A509xSCAC7Silamfrb2ogt3%2FsqCN5O8MRJkC8oQS%2BfPB%2FI%2B9HXsDg%2FvyewY14w5t0vPDXYbTPp6zxBic55MvruYajV43tcz5OwJqOfeK3bPILCeHKtHKJIm28xvNi3gYXWDy8Jjla5n8RHz1ABEp0NPOMyzMGNZTBjYxM6TFFCaKAQgTYbfeC8l5GLWc9Bh4ek2OnvHK4kOOlvJCzAz2tMwQZqbCEcP1T9VKVLeidGUjpeMYadARkpwf2OIxV3jjnCRmYlJdKcBwYB1HWOdxZgZ%2BxP4y7leGckZqnFAxVXrQr1whjlePLyu%2FzyMpOS4ydxqD5C4McBiF123XEYDZYlwTFfYLIyAUjEba5bGTy5co1E%2BTMVEe5ZoK2SjOVmaJSARVmpYKhnGpP1khFWjnVnmjUPRJP2n%2BgItD4HPjpcaf6WhjJdB3NGAlYShlp4qCRTNTqpL8HemMlFrlv5SVgasVL7L0rzPQxDpfh5uo5yOKcJFDGqtSxEFLLQmdxkDMUB7F86bVxkJiUnAZJGm7Ib%2BPrZyPo1FNkOrARFCD%2BJtgEsZ9S%2FV8mKD%2Fs1g%2FUleEQUOenFoh2AUEbchA0kHIIuleoy4eyioFsrkmT0C20HI6%2BzJZQbElYZ89wnAGCt5ZidQn11peyZNq993YenZpGnU5dt4XoLC5jwE3oh%2BiAmLKdUu27pklUaNzjXSomEAbXKaZJk%2FN1HnaUaxW1oZbzzFsXSfPr2JqY5c18ScQQjNw1H1%2BGbaUlLJx0BnLoBtKoBj0gWjrcphWey4JQDbhaEs0V61Amy98xmh1JNOvlxpafpzxOLo1kYEmjuR%2FJbUliGuiFaXh9glstR8sW83SO5%2FMMbYcrzXHavDuX9%2B7MAQxtqLTS%2Bdx8woucu64NRXidBsSvYFO7c66gUPAypIqVdXd4TSGQeaC09ML4L059%2BqAiI2v8luwe0tif0bj47wJNDO5DI4uTespTrFAso7vzo9kuyiPb0zCZESCl6kFnunXQqS9AhJ5KIfOidTNHYw%2FDG7BQma9ynmXjcWTntBg23P0uaLkfsCKH5gn9GELmVRZWDBTlNqUXeGmlHk21qYuaOJJeHDGUzSONU0sTqePw6TIXtcgdfnHEEOkyU2n4%2FdwFObrJEU8PmrOtl9IcP4M59ccX5EDn1ISeiFSpM3imnaYbjQJNAk02X0fAlnoeJ1J%2BhtlmkkGATs7oiUw1ciec66VTQxM6dXk6BW3ClJ8B24oVTF5gwyGqFSzFSVita7Ll7UzNmgaIJShvAkprbzcLTP4sYrwmf%2F5KdKhu5HMHGtShME6swE%2BAEyvDXUTB8w1tvJTR3bw4nM4iP0nCWR1cHGyLzwM5ybK6WzSB1inQttJYBWyoAWps7GUis0HCAUEmcvjI%2BauYd1JY8pX2AHGPyjlQeFRnUhAKCP96w5bYheXiOnR772%2FmGe8QQ2Vs0tcu5qBpZUVeeHQ5nvraYdBUO2yjIblLlE4EssWiEQpHumSbjFSL4A%2FgnYePDLr3wSIgsKHLS404L6sz5mGWHfAzICxwTAGYLyQ3COqoLC9yCgnNKUwqSKs8WD3agOC9NQnFJvbuD21iY5QehGLnwaR23S0bmh5IrkIgVmZ6Hht6sWwFtszj%2BpavtkA7hzZwfkM97LUtcnE4DaY%2BFWipiZMMUm8zfP3CMcOFW61e9lVpYdOXO6D8D7V5k8hApyb01CxHbQngAJWeR0myvdRPtniX6RFNfEn23hXR%2FTlrfwONT3HRFOSotQTapbEfz5jjcxLAL1m4y8Veyua6ymwnpLhUTWfGYIhoZ4zOpfplOBWDBDfJ9zKsYnxd%2BZRJ0lVA3%2Bmrn4nnlIZfpvgEywzkYFh2XT%2BYTTwyqMGClFYxgIs5pL8wJCP89iIbTapsTMerERdqySTyTUBfej8w21KVfMM7fkZP9pBY4%2FgO086th6bjfuo3kv07%2FyGIOE2ZN6CbzsjUzM%2Bh7B7O%2FOimuLAO5%2FOcK4Ik%2FDfrZpOTXoEw8nB0S0MpTcR4kicFwVI2oC9%2BZVTt8d4ocIyJZbLeukzmjDpxmG3PrD22rBdmz8CLRRL04teyoIx6mXVe2VWPWl1WZjmdp07OlFmch2W1tiPlJoxbl8CbJyf0I4KchuYiYbKNMuBcixhibNaJGGLSgTkHlwmhPY%2Fc%2FoWOq3Y5RFXoaNeQTlrsuP2UabXntizTmyDoWQA4tuUYyLXrj%2Bw5EuuJXst7f0M3hbkeccAY4HJxYEyA69SNEtSJUcLEChMPXLi9P%2BHAGKAartlG4clwzQqvH3bJQH4n4tMRVlM7KKMhIdnflimK28Q4Z4VnBmtEb0uKVLvzauvL4glizukuDvKFUK%2FWfhiJjDBwEIazBz3lOSNbVA73gT%2BncjV5JP8vwkiD1jXQ4315pBpuSvMeHW7Go74jgmyGT5NIF1%2BO7CG3Sk0SE9oKnoFrn5rQj9doQ20IesBNxLpeG6mKlC%2BTZWKZzyFg0Kw3r6xYg1O7wFCvd5UuFjivCLvOWk5%2FLr0tbX%2B6WugEfslwS1gQXHS74w2hDURLOk9j5HGCPKl59%2FmLLhYix%2BBlgbk6%2FnYFAM6yWEsyyQzrI%2FJ0jme7dQaGF2%2Ff1z0UnaaN%2BZqg2Jub7mi0JPq8uGePUtKR3t9SkyVVfFfwIerTHLHyXH8%2BFCAl6%2B72x4jaVGpIM%2BLYmBiGWedGk3g5gzoEjPXac6J6uQSOUvP0vCXXQyWcHFnr1OncOr0Ip0w46OBy6FaRKI3T7nXpZXwq2ul5RSLRWjPaTy1Xdv%2BhrdTCzQLH62KHEfJ%2BP3ZhTDCr2nQXgrvKY7vur5r2Vpl2dQpN9MfK3PdPsdk3ZzKqZyKNOgsNF08%2Bn7Fc2cbQbj9byDQU0NYpCrpoUlawuNC0h11P6IpB6luMv4ebLCoVpH4YHd%2FBcbaPQkJYsXmGP%2Ffgz74vM8L8uEsjuqNHPp4U%2FIu6UoP8EhargYWNIZ0%2BV3GRxNX1%2FJb29ly96iZcsYfsIQEU5g1ERtD215RX8v%2FJyH2wPOygpkd5Ba8FIVKtBj2oDw%2FpVjDOCjLb%2B%2Bt13rvsMnYR10fmTtcuXwYWLkblIrCnyiKwOFjjxyBjqXn4GM53WVeKGTNDs84VTytM0ylZVmWinp9szjcbK0%2BseNpEInVzzRiXtLOTJpU0fAeFcVtfP36C1dY50Dx1fz8JB0%2BbveOvlz716svM3rsi7t%2FOydeHi33meszCpGnT3kFrrPnFjuOG3kHukL6DJ%2BbdpkEUZLYi03GvdagcEFSccg0HDI32RNROiEjvq2ToFYD0xIXBJUO8rdqDLCypmi%2F4Jo0a8IXiTYG05gvZXTmAodemQJ4Ye9BwAQLPDFD5duze1S8J7bE0ypOOLGiyH7ttcYErD3EU0oerIsYxrqA2irfXoGwtd2%2B2bhmVVx%2BTuK7qKGmlxShVE50FDH1Wf2lXHlUa3hKmiF6OPjA0CtbrZmDKo7V7nXohVsVQhGSNVC1qr9wE5XeUajJBrWEdMsW70OnNL7KRCu2UW8M2rT9VqRRvQQLlqwHLfRT0Nygu4Qj5GIVuLNEUpJiF%2BfYDTZ1zlAcoTA1oWm0Zrda6QTY%2BAdj%2B7b1X%2ByGbeoSHf1w5qX1WC6uXp4S5jK1ZX%2BzaPqG1hx%2BfKeMm9BNpYXuHaSDfr5kX9KqaA0BcfPFPIBah6tNFrSTDbroqOka9T0khqs6VRP13SitpreoKxlSJ7%2FGuYbehZEcumq9ldwwaMuFvc96g2bBWu6%2BE%2Fx592e%2Bjj3%2B%2B%2BQv%2F%2BfUthKv%2F%2BW%2FHGkXEpDe%2FHCwkxrS4gp0gztTDXNMJq20nYX4CatPDyLpwgjlENVeJuYrE%2BKBBL3%2Fe3Lc0MPcbugixAod7%2FJQF10ZFVlc1%2BPitWvsEHzmNMU6rdEm%2BafUez6lF8Or%2F%3C%2Fdiagram%3E%3C%2Fmxfile%3E)

![initFlowChart](/flowchart/ProgramFlowchart.drawio.png)

The program's end configuration does differ in a few ways from the flowchart, primarily due to programming conventions and unplanned feature additions.

## Testing

All my testing information is contained in [TESTS.md](TESTS.md).

## How it Works

First, the program asks you if you want to create a booking, view a booking, or exit the program. 

### Create a Booking

The program will call upon the [actions.py](actions.py) file to run the `main()` function. This function will ask the user for input such as the age of the client, the source and destination of the trip, etc. Each of these inputs are placed into a loop by another related function, e.g. `get_valid_seat_count`, and the loop is only broken when a valid input is provided, creating in-built error-catching. For the destination/departure questions, the program, thanks to a modular display of the 3 cities, removes the city selected for departure from the print statement when prompting for the destination to prevent the user from entering the same city again. Even if they did it would make sure they tried again though.

I've kept the original cost, original seat count, and discount values static as in the context of the program, these are things that would be institutionally predetermined and wouldn't be prone to change at the end of the line. It would be unnecessary and allowing these to be user-determined would potentially create more errors and in-line problems down the road.

After all the information is taken, the program compiles the information into three classes from [data.py](data.py); Traveller, which contains the name and age of the client as well as the date of the flight, Flight, which generates a flight number for the booking and holds the route, fare, and available seat count, and finally, Booking, which takes the previous two classes for it's own, as well as calculating the final fare by holding the discount data.

After the classes are populated, the program uses the `EmailGenerator` class' `generate_email()` function to create the copy-pastable email for the user. At which point it promptly paduks it out into the terminal, saves it to the CSV file *(to access later should the user wish)* with a confirmation message, and then asks the user if they want to send the email at that moment.

If they do want to send the email, the program will create a `mailto:` link that will auto-populate the user's default mail client with the body and subject of the flight email to send immediately. 

If they don't want to send the email, then the program will return to the beginning, and maybe end; like this section of the guide will right now.

### View a Booking

Simply simple. Simpledeedoo da.

The program now will run the `load_booking_by_name()` function in [actions.py](actions.py). 

First, the function calls the csv file, parses it for it's name column values, and lists them to the user to display the existing names within the file.

This function will then ask the user the name of the person who's booking they want to access. The program will open the csv file in 'read' mode, and it parses the file contents to search for the name provided.

After it finds the user's row in the csv file, it takes the data, prints it into a summary, and it recreates the class structure with the variables from the csv, and then it recreates the email and displays it. 

It also once again prompts the user if they want to send the email now, using the `mailto:` link function from before.

### Exit the Program

...\
...\
Goodbai...