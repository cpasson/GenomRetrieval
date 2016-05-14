#!/home/bif712_153a20/software/bin/perl

use strict;
use warnings;
use LWP::Simple;
use CGI;
#use CGI::Carp "fatalsToBrowser";


my ($page, @lines, $okToPrint, $stopPrint, $virus, $url, $cgi, @genBankData, @lines, $test, @referencePortion, @authorsPortion, @pubmedPortion, $originSection, $countT, $countA, $countC, $countG, @journalPortion, @journalPortionPrint, @titlePortion, $email, @elementInput);

$cgi = new CGI;

print $cgi->header ();
print $cgi->start_html;

@genBankData = $cgi->param('attributes');  # grabbing user entered information from the generic genBank html form
$virus = $cgi->param('viruses');

my @virusFile = split('/', $virus); # splitting the long virus name into two pieces

$virus = $virusFile[1]; # only want the NC_... part

$url = "ftp://ftp.ncbi.nih.gov/genomes/Viruses/";
# $url .= $virus;

# print "Content-type: text/html\n\n";
print "<html><body><pre>\n";
#print "virus chosen: '$virus'\n";

## lines 60 - 160: extracting the proper virus page from ncbi, if the file has already be accessed it will open the file rather than re-download the file

if($virus eq "NC_004777.gbk") {
	
 	if(!(-f "NC_004777.gbk")) {
    	print "why am I not here in the -f if( )...\n";
   		$page = get("ftp://ftp.ncbi.nih.gov/genomes/Viruses/Yersinia_pestis_phage_phiA1122_uid14332/NC_004777.gbk");
   		die "Error retrieving GenBank file from NCBI..." unless defined($page);
   		open(FD, "> $virus") || die("Error opening file... $!\n");
   		print FD "$page";
   		close(FD);
    }
    else {
    	$/ = undef;   # default record separator is undefined
		open(FD, "< $virus") || die("Error opening file: '$virus'\n $!\n");
		$page = <FD>; # file slurp (reads the entire file into a scalar)
		close(FD);
		$/ = "\n";    # resets the default record back to newline

       #print "$page\n";
    }
}

elsif($virus eq "NC_002549.gbk") {
	if(!(-f "NC_002549.gbk")) {
   		$page = get("ftp://ftp.ncbi.nih.gov/genomes/Viruses/Zaire_ebolavirus_uid14703/NC_002549.gbk");
   		die "Error retrieving GenBank file from NCBI..." unless defined($page);
   		open(FD, "> $virus") || die("Error opening file... $!\n");
        #print "$page\n";
   		print FD "$page";
   		close(FD);
   	}
   	else {
   		$/ = undef;   # default record separator is undefined
		open(FD, "< $virus") || die("Error opening file: '$virus'\n $!\n");
		$page = <FD>; # file slurp (reads the entire file into a scalar)
		close(FD);
		$/ = "\n";    # resets the default record back to newline

       #print "$page\n";
   	}
}

elsif($virus eq "NC_001781.gbk") {
	if(!(-f "NC_001781.gbk")) {
   		$page = get("ftp://ftp.ncbi.nih.gov/genomes/Viruses/Human_respiratory_syncytial_virus_uid15003/NC_001781.gbk");
   		die "Error retrieving GenBank file from NCBI..." unless defined($page);
   		open(FD, "> $virus") || die("Error opening file... $!\n");

   		print FD "$page";
   		close(FD);
   	}
   	else {
   		$/ = undef;   # default record separator is undefined
		open(FD, "< $virus") || die("Error opening file: '$virus'\n $!\n");
		$page = <FD>; # file slurp (reads the entire file into a scalar)
		close(FD);
		$/ = "\n";    # resets the default record back to newline

       #print "$page\n";
    }
}

elsif($virus eq "NC_004763.gbk") {
	if(!(-f "NC_004763.gbk")) {
   		$page = get("ftp://ftp.ncbi.nih.gov/genomes/Viruses/African_green_monkey_polyomavirus_uid15320/NC_004763.gbk");
   		die "Error retrieving GenBank file from NCBI..." unless defined($page);
   		open(FD, "> $virus") || die("Error opening file... $!\n");

   		print FD "$page";
   		close(FD);
   	}
   	else {
   		$/ = undef;   # default record separator is undefined
		open(FD, "< $virus") || die("Error opening file: '$virus'\n $!\n");
		$page = <FD>; # file slurp (reads the entire file into a scalar)
		close(FD);
		$/ = "\n";    # resets the default record back to newline

       #print "$page\n";
   	}
}

elsif($virus eq "NC_004679.gbk") {
	if(!(-f "NC_004679.gbk")) {
   		$page = get("ftp://ftp.ncbi.nih.gov/genomes/Viruses/Staphylococcus_aureus_phage_P68_uid14269/NC_004679.gbk");
   		die "Error retrieving GenBank file from NCBI..." unless defined($page);
   		open(FD, "> $virus") || die("Error opening file... $!\n");

   		print FD "$page";
   		close(FD);
   	}
   	else {
   		$/ = undef;   # default record separator is undefined
		open(FD, "< $virus") || die("Error opening file: '$virus'\n $!\n");
		$page = <FD>; # file slurp (reads the entire file into a scalar)
		close(FD);
		$/ = "\n";    # resets the default record back to newline

       #print "$page\n";
   	}
}

# -----------------------------------------------------------------------------

#print "checkboxes selected... @genBankData\n";

@lines = split('\n', $page);  # takes the proper virus that was selected from form and splits it up at each new line

foreach(@genBankData) { # foreach of the different attributes selected from the form it will run through all these if statements

if(scalar(@genBankData == 15)) { # if the user 'selects all' it will only perform this if statement, and then print the entire page
#print "$page";
last;
}

if($_ eq "LOCUS") {

    $okToPrint = $stopPrint = 0;

    foreach(@lines) {

        $okToPrint = 1 if($_ =~ m/^LOCUS/);
        $stopPrint = 1 if($_ =~ m/^DEFINITION/);

            if($okToPrint  == 1 && $stopPrint == 0) {
            $test .= "$_\n";
            }

            if ($stopPrint == 1) {
            #print " second test $test";
            last;
            }  
    }    
}

if($_ eq "DEFINITION") {

    $okToPrint = $stopPrint = 0;

    foreach(@lines) {

        $okToPrint = 1 if($_ =~ m/^DEFINITION/);
        $stopPrint = 1 if($_ =~ m/^ACCESSION/);


            if($okToPrint  == 1 && $stopPrint == 0) {
            $test .= "$_\n";
            }

            if ($stopPrint == 1) { 
            #print $test;
            last;
            }
    }        
}

if($_ eq "ACCESSION") {
    
    $okToPrint = $stopPrint = 0;

    foreach(@lines) {

        $okToPrint = 1 if($_ =~ m/^ACCESSION/);
        $stopPrint = 1 if($_ =~ m/^VERSION/);

            if($okToPrint  == 1 && $stopPrint == 0) {
            $test .= "$_\n";
            }

            if ($stopPrint == 1) {
            #print $test;
            last;  
            }
    }
}

if($_ eq "VERSION") {
    
    $okToPrint = $stopPrint = 0;

    foreach(@lines) {

        $okToPrint = 1 if($_ =~ m/VERSION/);
        $stopPrint = 1 if($_ =~ m/^DBLINK/);

            if($okToPrint  == 1 && $stopPrint == 0) {
            $test .= "$_\n";
            }

            if ($stopPrint == 1) {
            #print $test;
            last;  
            }
    }      
}

if($_ eq "KEYWORDS") {
    
    $okToPrint = $stopPrint = 0;

    foreach(@lines) {

        $okToPrint = 1 if($_ =~ m/KEYWORDS/);
        $stopPrint = 1 if($_ =~ m/^SOURCE/);

            if($okToPrint  == 1 && $stopPrint == 0) {
            $test .= "$_\n";
            }

            if ($stopPrint == 1) {
            #print $test;
            last;
            }
    }
}

if($_ eq "SOURCE") {
    
    $okToPrint = $stopPrint = 0;

    foreach(@lines) {

        $okToPrint = 1 if($_ =~ m/^SOURCE/);
        $stopPrint = 1 if($_ =~ m/^REFERENCE/);

            if($okToPrint  == 1 && $stopPrint == 0) {
            $test .= "$_\n";
            }

            if ($stopPrint == 1) {
            #print $test;
            last; 
            }
    }
}

if($_ eq "ORGANISM") {
    
    $okToPrint = $stopPrint = 0;

    foreach(@lines) {

        $okToPrint = 1 if($_ =~ m/ORGANISM/);
        $stopPrint = 1 if($_ =~ m/^REFERENCE/);

            if($okToPrint  == 1 && $stopPrint == 0) {
            $test .= "$_\n";
            }

            if ($stopPrint == 1) {
            #print $test;
            last;
            }
    }
}

# used grep command for these attributes because they occur more than once within the page, journal was most difficult regular expression because could end after several different entries

if ( grep( /^REFERENCE/, @genBankData ) ){
  @referencePortion = ($page =~ /(REFERENCE.*?)COMMENT/s);
}

if ( grep( /^AUTHORS/, @genBankData ) ){
  @authorsPortion = ($page =~ /(  AUTHORS.*?)  TITLE+/gs);
}

if ( grep( /^TITLE/, @genBankData ) ){
  @titlePortion = ($page =~ /(  TITLE.*?)  JOURNAL+/gs);
}

if ( grep( /^JOURNAL/, @genBankData ) ){
  @journalPortion = ($page =~ /\s\s(JOURNAL.*?)\s(?=PUBMED|REFERENCE|JOURNAL|REMARK|COMMENT)/gs);
}

if ( grep( /^MEDLINE/, @genBankData ) ){
  @pubmedPortion = ($page =~ /(   PUBMED.*?)REFERENCE+/gs);
}

if($_ eq "FEATURES") {
    
    $okToPrint = $stopPrint = 0;

    foreach(@lines) {

        $okToPrint = 1 if($_ =~ m/FEATURES/);
        $stopPrint = 1 if($_ =~ m/^ORIGIN/);

            if($okToPrint  == 1 && $stopPrint == 0) {
            $test .= "$_\n";
            }

            if ($stopPrint == 1) {
            #print $test;
            last;
       
            }
    }

}

if($_ eq "BASECOUNT") { # grab the origin section, and then use the transiterate function to count the number of times each 'a', 'c', 'g', 't' occurs (don't have to worry about the 'G' in ORIGIN because only matched lower case letters)
    
    $okToPrint = $stopPrint = 0;

    foreach(@lines) {

        $okToPrint = 1 if($_ =~ m/^ORIGIN/);
        $stopPrint = 1 if($_ =~ m/^\//);
        
            if($okToPrint  == 1 && $stopPrint == 0) {
            $originSection .= "$_\n";  
            }
        
    }

    $countT = $originSection =~ tr/t//;
    $countA = $originSection =~ tr/a//;
    $countC = $originSection =~ tr/c//;
    $countG = $originSection =~ tr/g//;

    $test .= "BASE COUNT      $countA A     $countC C     $countG G     $countT T\n";
}
}  

if($_ eq "ORIGIN") {
    
    $okToPrint = $stopPrint = 0;

    foreach(@lines) {

        $okToPrint = 1 if($_ =~ m/^ORIGIN/);
        $stopPrint = 1 if($_ =~ m/^\//);

            if($okToPrint  == 1 && $stopPrint == 0) {
            $test .= "$_\n";
            }

            if ($stopPrint == 1) {
            #print $test;
            last;
            }
    }
}

my @completeArray = $test; # need to combine all the different print elements into one array, first added $test scalar to new array
my @mergedArray = (@completeArray, @referencePortion, @authorsPortion, @titlePortion, @journalPortion, @pubmedPortion); # then added all the arrays to a merged array

#print @mergedArray;
#print @completeArray;
#print "$test\n";
#print @referencePortion;
#print @authorsPortion;
#print @titlePortion;
#print @journalPortion;
#print @pubmedPortion;

$email = $cgi->param('mailto');

emailValidate($email);

sub emailValidate($) { # subroutine to validate email
    if($email =~/(^([a-zA-Z-\..]{2,})*([^-\.])@([a-zA-Z-\.{2,}]*)([^-][\.])[a-zA-Z]{2,4})/) {
        my $mailRef = "| /usr/bin/mail -s $virus " . $email;
        open(MAIL,$mailRef);
            unless(@genBankData == 15) { # as long as the user hasn't 'select all' the form only print what was selected
                print MAIL @mergedArray; # prints what has been selected to email
            }
            else {
                print MAIL $page; # if the user 'select all' then just print the entire page to email
                print $page;   # prints entire page to the web screen
            }

        close(MAIL);
        print "@mergedArray\n\n"; # prints proper portion of selected items to web screen
    }

    else {
    print "Email entered is not valid\n"; # prints error if email isn't validated by regular expression
    }    
} 

exit;
print "</pre></body></html>\n";

print $cgi->end_html ();



