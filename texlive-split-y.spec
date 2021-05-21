%global tl_version 2018
%global _texdir %{_datadir}/texlive
%global __brp_mangle_shebangs /usr/bin/true

Name:           texlive-split-y
Version:        %{tl_version}
Release:        24
Epoch:          8
Summary:        TeX formatting system
License:        Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0003:     texlive-licenses.tar.xz
Source1245:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uhc.tar.xz
Source1246:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uhc.doc.tar.xz
Source1247:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wadalab.tar.xz
Source1248:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wadalab.doc.tar.xz
Source1428:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/url.tar.xz
Source1429:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/url.doc.tar.xz
Source1519:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uni-wtal-ger.tar.xz
Source1520:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uni-wtal-ger.doc.tar.xz
Source1521:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uni-wtal-lin.tar.xz
Source1522:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uni-wtal-lin.doc.tar.xz
Source1526:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/usebib.tar.xz
Source1527:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/usebib.doc.tar.xz
Source1529:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/vak.tar.xz
Source1530:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/vak.doc.tar.xz
Source2095:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/umtypewriter.tar.xz
Source2096:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/universa.tar.xz
Source2097:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/universa.doc.tar.xz
Source2099:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/universalis.tar.xz
Source2100:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/universalis.doc.tar.xz
Source2101:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/urwchancal.tar.xz
Source2102:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/urwchancal.doc.tar.xz
Source2103:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/venturisadf.tar.xz
Source2104:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/venturisadf.doc.tar.xz
Source2106:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wsuipa.tar.xz
Source2107:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wsuipa.doc.tar.xz
Source2154:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/utopia.tar.xz
Source2155:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/utopia.doc.tar.xz
Source2156:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wasy.tar.xz
Source2157:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wasy.doc.tar.xz
Source2158:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wasy2-ps.tar.xz
Source2159:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wasy2-ps.doc.tar.xz
Source2160:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wasysym.tar.xz
Source2161:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wasysym.doc.tar.xz
Source2337:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/upca.tar.xz
Source2338:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/upca.doc.tar.xz
Source2359:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ulem.tar.xz
Source2360:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ulem.doc.tar.xz
Source2480:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/verse.tar.xz
Source2481:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/verse.doc.tar.xz
Source2560:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ukrhyph.tar.xz
Source2561:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ukrhyph.doc.tar.xz
Source2662:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/visualfaq.doc.tar.xz
Source2664:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/webguide.doc.tar.xz
Source2739:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/variations.tar.xz
Source2740:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/variations.doc.tar.xz
Source2790:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/udesoftec.tar.xz
Source2791:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/udesoftec.doc.tar.xz
Source2793:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/umlaute.tar.xz
Source2794:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/umlaute.doc.tar.xz
Source2796:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/voss-mathcol.doc.tar.xz
Source2848:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wnri.tar.xz
Source2849:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wnri.doc.tar.xz
Source2850:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wnri-latex.tar.xz
Source2851:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wnri-latex.doc.tar.xz
Source2946:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/vntex.tar.xz
Source2947:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/vntex.doc.tar.xz
Source2973:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/utf8mex.tar.xz
Source2974:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/utf8mex.doc.tar.xz
Source3106:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/underscore.tar.xz
Source3107:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/underscore.doc.tar.xz
Source3383:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/venndiagram.tar.xz
Source3384:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/venndiagram.doc.tar.xz
Source5587:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uassign.tar.xz
Source5588:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uassign.doc.tar.xz
Source5589:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ucs.tar.xz
Source5590:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ucs.doc.tar.xz
Source5591:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uebungsblatt.tar.xz
Source5592:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uebungsblatt.doc.tar.xz
Source5593:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/umoline.tar.xz
Source5594:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/umoline.doc.tar.xz
Source5596:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/underlin.tar.xz
Source5597:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/underlin.doc.tar.xz
Source5599:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/underoverlap.tar.xz
Source5600:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/underoverlap.doc.tar.xz
Source5601:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/undolabl.tar.xz
Source5602:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/undolabl.doc.tar.xz
Source5604:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/units.tar.xz
Source5605:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/units.doc.tar.xz
Source5607:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/unravel.tar.xz
Source5608:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/unravel.doc.tar.xz
Source5610:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/upmethodology.tar.xz
Source5611:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/upmethodology.doc.tar.xz
Source5612:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/upquote.tar.xz
Source5613:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/upquote.doc.tar.xz
Source5615:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uri.tar.xz
Source5616:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uri.doc.tar.xz
Source5618:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ushort.tar.xz
Source5619:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ushort.doc.tar.xz
Source5621:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/varindex.tar.xz
Source5622:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/varindex.doc.tar.xz
Source5624:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/varsfromjobname.tar.xz
Source5625:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/varsfromjobname.doc.tar.xz
Source5626:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/varwidth.tar.xz
Source5627:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/varwidth.doc.tar.xz
Source5628:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/vdmlisting.tar.xz
Source5629:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/vdmlisting.doc.tar.xz
Source5630:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/verbasef.tar.xz
Source5631:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/verbasef.doc.tar.xz
Source5632:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/verbatimbox.tar.xz
Source5633:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/verbatimbox.doc.tar.xz
Source5634:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/verbatimcopy.tar.xz
Source5635:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/verbatimcopy.doc.tar.xz
Source5636:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/verbdef.tar.xz
Source5637:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/verbdef.doc.tar.xz
Source5638:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/verbments.tar.xz
Source5639:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/verbments.doc.tar.xz
Source5640:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/version.tar.xz
Source5641:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/version.doc.tar.xz
Source5642:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/versions.tar.xz
Source5643:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/versions.doc.tar.xz
Source5644:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/versonotes.tar.xz
Source5645:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/versonotes.doc.tar.xz
Source5647:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/vertbars.tar.xz
Source5648:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/vertbars.doc.tar.xz
Source5650:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/vgrid.tar.xz
Source5651:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/vgrid.doc.tar.xz
Source5653:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/vhistory.tar.xz
Source5654:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/vhistory.doc.tar.xz
Source5655:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/vmargin.tar.xz
Source5656:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/vmargin.doc.tar.xz
Source5658:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/volumes.tar.xz
Source5659:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/volumes.doc.tar.xz
Source5663:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/vruler.tar.xz
Source5664:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/vruler.doc.tar.xz
Source5665:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/vwcol.tar.xz
Source5666:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/vwcol.doc.tar.xz
Source5668:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wallpaper.tar.xz
Source5669:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wallpaper.doc.tar.xz
Source5670:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/warning.tar.xz
Source5671:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/warning.doc.tar.xz
Source5672:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/warpcol.tar.xz
Source5673:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/warpcol.doc.tar.xz
Source5675:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/was.tar.xz
Source5676:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/was.doc.tar.xz
Source5678:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/widetable.tar.xz
Source5679:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/widetable.doc.tar.xz
Source5681:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/williams.tar.xz
Source5682:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/williams.doc.tar.xz
Source5683:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/withargs.tar.xz
Source5684:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/withargs.doc.tar.xz
Source5685:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wordlike.tar.xz
Source5686:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wordlike.doc.tar.xz
Source5688:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wrapfig.tar.xz
Source5689:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wrapfig.doc.tar.xz
Source5821:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ucharcat.tar.xz
Source5822:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ucharcat.doc.tar.xz
Source5935:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/unicode-math.tar.xz
Source5936:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/unicode-math.doc.tar.xz
Source5938:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/venn.tar.xz
Source5939:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/venn.doc.tar.xz
Source6116:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/varisize.tar.xz
Source6117:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/varisize.doc.tar.xz
Source6330:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uml.tar.xz
Source6331:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uml.doc.tar.xz
Source6333:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/vaucanson-g.tar.xz
Source6334:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/vaucanson-g.doc.tar.xz
Source6335:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/vocaltract.tar.xz
Source6336:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/vocaltract.doc.tar.xz
Source6570:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uaclasses.tar.xz
Source6571:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uaclasses.doc.tar.xz
Source6576:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uafthesis.tar.xz
Source6577:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uafthesis.doc.tar.xz
Source6578:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ucbthesis.tar.xz
Source6579:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ucbthesis.doc.tar.xz
Source6580:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ucdavisthesis.tar.xz
Source6581:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ucdavisthesis.doc.tar.xz
Source6583:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ucthesis.tar.xz
Source6584:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ucthesis.doc.tar.xz
Source6585:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uestcthesis.tar.xz
Source6586:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uestcthesis.doc.tar.xz
Source6587:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uiucredborder.tar.xz
Source6588:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uiucredborder.doc.tar.xz
Source6590:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uiucthesis.tar.xz
Source6591:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uiucthesis.doc.tar.xz
Source6593:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ulthese.tar.xz
Source6594:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ulthese.doc.tar.xz
Source6596:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/umthesis.tar.xz
Source6597:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/umthesis.doc.tar.xz
Source6598:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/umich-thesis.tar.xz
Source6599:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/umich-thesis.doc.tar.xz
Source6600:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/unamth-template.doc.tar.xz
Source6601:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/unamthesis.tar.xz
Source6602:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/unamthesis.doc.tar.xz
Source6603:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/unswcover.tar.xz
Source6604:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/unswcover.doc.tar.xz
Source6605:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uothesis.tar.xz
Source6606:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uothesis.doc.tar.xz
Source6608:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/urcls.tar.xz
Source6609:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/urcls.doc.tar.xz
Source6610:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uowthesis.tar.xz
Source6611:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uowthesis.doc.tar.xz
Source6612:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uowthesistitlepage.tar.xz
Source6613:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uowthesistitlepage.doc.tar.xz
Source6614:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uspatent.tar.xz
Source6615:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uspatent.doc.tar.xz
Source6616:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ut-thesis.tar.xz
Source6617:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ut-thesis.doc.tar.xz
Source6618:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uwthesis.tar.xz
Source6619:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uwthesis.doc.tar.xz
Source6620:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/vancouver.tar.xz
Source6621:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/vancouver.doc.tar.xz
Source6622:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wsemclassic.tar.xz
Source6623:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wsemclassic.doc.tar.xz
Source6741:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/unitsdef.tar.xz
Source6742:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/unitsdef.doc.tar.xz
Source6775:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ucharclasses.tar.xz
Source6776:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ucharclasses.doc.tar.xz
Source6777:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/unisugar.tar.xz
Source6778:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/unisugar.doc.tar.xz
Source7534:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uantwerpendocs.tar.xz
Source7535:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uantwerpendocs.doc.tar.xz
Source7537:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uhrzeit.tar.xz
Source7538:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uhrzeit.doc.tar.xz
Source7539:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/umbclegislation.tar.xz
Source7540:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/umbclegislation.doc.tar.xz
Source7541:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/unicode-data.tar.xz
Source7542:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/unicode-data.doc.tar.xz
Source7543:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/updmap-map.tar.xz
Source7544:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uplatex.tar.xz
Source7550:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/visualpstricks.doc.tar.xz
Source7551:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/visualtikz.doc.tar.xz
Source7586:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uptex-base.tar.xz
Source7587:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uptex-base.doc.tar.xz
Source7588:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uptex-fonts.tar.xz
Source7589:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uptex-fonts.doc.tar.xz
Source7990:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uhhassignment.tar.xz
Source7991:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uhhassignment.doc.tar.xz
Source7993:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/undergradmath.doc.tar.xz
Source7994:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/unfonts-core.tar.xz
Source7995:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/unfonts-core.doc.tar.xz
Source7996:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/unfonts-extra.tar.xz
Source7997:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/unfonts-extra.doc.tar.xz
Source7998:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/unicode-bidi.tar.xz
Source7999:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/unicode-bidi.doc.tar.xz
Source8000:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/unitn-bimrep.tar.xz
Source8001:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/unitn-bimrep.doc.tar.xz
Source8002:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/upzhkinsoku.tar.xz
Source8003:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/upzhkinsoku.doc.tar.xz
Source8004:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uspace.tar.xz
Source8005:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uspace.doc.tar.xz
Source8008:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/variablelm.tar.xz
Source8009:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/variablelm.doc.tar.xz
Source8012:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wallcalendar.tar.xz
Source8013:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wallcalendar.doc.tar.xz
Source8014:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wtref.tar.xz
Source8015:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wtref.doc.tar.xz
Source8376:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ucsmonograph.tar.xz
Source8377:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ucsmonograph.doc.tar.xz
Source8378:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/univie-ling.tar.xz
Source8379:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/univie-ling.doc.tar.xz
Source8380:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uppunctlm.tar.xz
Source8381:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uppunctlm.doc.tar.xz
Source8382:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/witharrows.tar.xz
Source8383:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/witharrows.doc.tar.xz

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.

%package -n texlive-udesoftec
Provides:       tex-udesoftec = %{tl_version}
License:        LPPL 1.3
Summary:        Thesis class for the University of Duisburg-Essen
Version:        svn47164
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xstring.sty), tex(babel.sty), tex(csquotes.sty), tex(regexpatch.sty)
Requires:       tex(hyperref.sty), tex(hyphenat.sty), tex(scrbase.sty), tex(nag.sty)
Provides:       tex(udesoftec-bibcommon.sty) = %{tl_version}
Provides:       tex(udesoftec-biblatex.sty) = %{tl_version}
Provides:       tex(udesoftec-bst.sty) = %{tl_version}, tex(udesoftec-extra.sty) = %{tl_version}
Provides:       tex(udesoftec.cls) = %{tl_version}

%description -n texlive-udesoftec
The class is designed for typesetting theses in the Research
Group for Business Informatics and Software Engineering. (The
class may also serve as a template for such theses.) The class
is designed for use with pdfLaTeX; input in UTF-8 encoding is
assumed.

%package -n texlive-udesoftec-doc
Summary:        Documentation for udesoftec
Version:        svn44308
Provides:       tex-udesoftec-doc
AutoReqProv:    No

%description -n texlive-udesoftec-doc
Documentation for udesoftec

%package -n texlive-uhc
Provides:       tex-uhc = %{tl_version}
License:        LPPL
Summary:        Fonts for the Korean language
Version:        svn16791.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(umj.map) = %{tl_version}, tex(umj00.tfm) = %{tl_version}
Provides:       tex(umj01.tfm) = %{tl_version}, tex(umj02.tfm) = %{tl_version}
Provides:       tex(umj03.tfm) = %{tl_version}, tex(umj04.tfm) = %{tl_version}
Provides:       tex(umj05.tfm) = %{tl_version}, tex(umj10.tfm) = %{tl_version}
Provides:       tex(umj11.tfm) = %{tl_version}, tex(umj12.tfm) = %{tl_version}
Provides:       tex(umj13.tfm) = %{tl_version}, tex(umj14.tfm) = %{tl_version}
Provides:       tex(umj15.tfm) = %{tl_version}, tex(umj16.tfm) = %{tl_version}
Provides:       tex(umj17.tfm) = %{tl_version}, tex(umj20.tfm) = %{tl_version}
Provides:       tex(umj21.tfm) = %{tl_version}, tex(umj22.tfm) = %{tl_version}
Provides:       tex(umj23.tfm) = %{tl_version}, tex(umj24.tfm) = %{tl_version}
Provides:       tex(umj25.tfm) = %{tl_version}, tex(umj26.tfm) = %{tl_version}
Provides:       tex(umj27.tfm) = %{tl_version}, tex(umj28.tfm) = %{tl_version}
Provides:       tex(umj29.tfm) = %{tl_version}, tex(umj30.tfm) = %{tl_version}
Provides:       tex(umj31.tfm) = %{tl_version}, tex(umj32.tfm) = %{tl_version}
Provides:       tex(umj33.tfm) = %{tl_version}, tex(umj34.tfm) = %{tl_version}
Provides:       tex(umj35.tfm) = %{tl_version}, tex(umj36.tfm) = %{tl_version}
Provides:       tex(umj37.tfm) = %{tl_version}, tex(umj38.tfm) = %{tl_version}
Provides:       tex(umjc00.tfm) = %{tl_version}, tex(umjc01.tfm) = %{tl_version}
Provides:       tex(umjc02.tfm) = %{tl_version}, tex(umjc03.tfm) = %{tl_version}
Provides:       tex(umjc04.tfm) = %{tl_version}, tex(umjc05.tfm) = %{tl_version}
Provides:       tex(umjc10.tfm) = %{tl_version}, tex(umjc11.tfm) = %{tl_version}
Provides:       tex(umjc12.tfm) = %{tl_version}, tex(umjc13.tfm) = %{tl_version}
Provides:       tex(umjc14.tfm) = %{tl_version}, tex(umjc15.tfm) = %{tl_version}
Provides:       tex(umjc16.tfm) = %{tl_version}, tex(umjc17.tfm) = %{tl_version}
Provides:       tex(umjc20.tfm) = %{tl_version}, tex(umjc21.tfm) = %{tl_version}
Provides:       tex(umjc22.tfm) = %{tl_version}, tex(umjc23.tfm) = %{tl_version}
Provides:       tex(umjc24.tfm) = %{tl_version}, tex(umjc25.tfm) = %{tl_version}
Provides:       tex(umjc26.tfm) = %{tl_version}, tex(umjc27.tfm) = %{tl_version}
Provides:       tex(umjc28.tfm) = %{tl_version}, tex(umjc29.tfm) = %{tl_version}
Provides:       tex(umjc30.tfm) = %{tl_version}, tex(umjc31.tfm) = %{tl_version}
Provides:       tex(umjc32.tfm) = %{tl_version}, tex(umjc33.tfm) = %{tl_version}
Provides:       tex(umjc34.tfm) = %{tl_version}, tex(umjc35.tfm) = %{tl_version}
Provides:       tex(umjc36.tfm) = %{tl_version}, tex(umjc37.tfm) = %{tl_version}
Provides:       tex(umjc38.tfm) = %{tl_version}, tex(umjco00.tfm) = %{tl_version}
Provides:       tex(umjco01.tfm) = %{tl_version}, tex(umjco02.tfm) = %{tl_version}
Provides:       tex(umjco03.tfm) = %{tl_version}, tex(umjco04.tfm) = %{tl_version}
Provides:       tex(umjco05.tfm) = %{tl_version}, tex(umjco10.tfm) = %{tl_version}
Provides:       tex(umjco11.tfm) = %{tl_version}, tex(umjco12.tfm) = %{tl_version}
Provides:       tex(umjco13.tfm) = %{tl_version}, tex(umjco14.tfm) = %{tl_version}
Provides:       tex(umjco15.tfm) = %{tl_version}, tex(umjco16.tfm) = %{tl_version}
Provides:       tex(umjco17.tfm) = %{tl_version}, tex(umjco20.tfm) = %{tl_version}
Provides:       tex(umjco21.tfm) = %{tl_version}, tex(umjco22.tfm) = %{tl_version}
Provides:       tex(umjco23.tfm) = %{tl_version}, tex(umjco24.tfm) = %{tl_version}
Provides:       tex(umjco25.tfm) = %{tl_version}, tex(umjco26.tfm) = %{tl_version}
Provides:       tex(umjco27.tfm) = %{tl_version}, tex(umjco28.tfm) = %{tl_version}
Provides:       tex(umjco29.tfm) = %{tl_version}, tex(umjco30.tfm) = %{tl_version}
Provides:       tex(umjco31.tfm) = %{tl_version}, tex(umjco32.tfm) = %{tl_version}
Provides:       tex(umjco33.tfm) = %{tl_version}, tex(umjco34.tfm) = %{tl_version}
Provides:       tex(umjco35.tfm) = %{tl_version}, tex(umjco36.tfm) = %{tl_version}
Provides:       tex(umjco37.tfm) = %{tl_version}, tex(umjco38.tfm) = %{tl_version}
Provides:       tex(umjo00.tfm) = %{tl_version}, tex(umjo01.tfm) = %{tl_version}
Provides:       tex(umjo02.tfm) = %{tl_version}, tex(umjo03.tfm) = %{tl_version}
Provides:       tex(umjo04.tfm) = %{tl_version}, tex(umjo05.tfm) = %{tl_version}
Provides:       tex(umjo10.tfm) = %{tl_version}, tex(umjo11.tfm) = %{tl_version}
Provides:       tex(umjo12.tfm) = %{tl_version}, tex(umjo13.tfm) = %{tl_version}
Provides:       tex(umjo14.tfm) = %{tl_version}, tex(umjo15.tfm) = %{tl_version}
Provides:       tex(umjo16.tfm) = %{tl_version}, tex(umjo17.tfm) = %{tl_version}
Provides:       tex(umjo20.tfm) = %{tl_version}, tex(umjo21.tfm) = %{tl_version}
Provides:       tex(umjo22.tfm) = %{tl_version}, tex(umjo23.tfm) = %{tl_version}
Provides:       tex(umjo24.tfm) = %{tl_version}, tex(umjo25.tfm) = %{tl_version}
Provides:       tex(umjo26.tfm) = %{tl_version}, tex(umjo27.tfm) = %{tl_version}
Provides:       tex(umjo28.tfm) = %{tl_version}, tex(umjo29.tfm) = %{tl_version}
Provides:       tex(umjo30.tfm) = %{tl_version}, tex(umjo31.tfm) = %{tl_version}
Provides:       tex(umjo32.tfm) = %{tl_version}, tex(umjo33.tfm) = %{tl_version}
Provides:       tex(umjo34.tfm) = %{tl_version}, tex(umjo35.tfm) = %{tl_version}
Provides:       tex(umjo36.tfm) = %{tl_version}, tex(umjo37.tfm) = %{tl_version}
Provides:       tex(umjo38.tfm) = %{tl_version}, tex(umju00.tfm) = %{tl_version}
Provides:       tex(umju01.tfm) = %{tl_version}, tex(umju02.tfm) = %{tl_version}
Provides:       tex(umju03.tfm) = %{tl_version}, tex(umju04.tfm) = %{tl_version}
Provides:       tex(umju05.tfm) = %{tl_version}, tex(umju10.tfm) = %{tl_version}
Provides:       tex(umju11.tfm) = %{tl_version}, tex(umju12.tfm) = %{tl_version}
Provides:       tex(umju13.tfm) = %{tl_version}, tex(umju14.tfm) = %{tl_version}
Provides:       tex(umju15.tfm) = %{tl_version}, tex(umju16.tfm) = %{tl_version}
Provides:       tex(umju17.tfm) = %{tl_version}, tex(umju20.tfm) = %{tl_version}
Provides:       tex(umju21.tfm) = %{tl_version}, tex(umju22.tfm) = %{tl_version}
Provides:       tex(umju23.tfm) = %{tl_version}, tex(umju24.tfm) = %{tl_version}
Provides:       tex(umju25.tfm) = %{tl_version}, tex(umju26.tfm) = %{tl_version}
Provides:       tex(umju27.tfm) = %{tl_version}, tex(umju28.tfm) = %{tl_version}
Provides:       tex(umju29.tfm) = %{tl_version}, tex(umju30.tfm) = %{tl_version}
Provides:       tex(umju31.tfm) = %{tl_version}, tex(umju32.tfm) = %{tl_version}
Provides:       tex(umju33.tfm) = %{tl_version}, tex(umju34.tfm) = %{tl_version}
Provides:       tex(umju35.tfm) = %{tl_version}, tex(umju36.tfm) = %{tl_version}
Provides:       tex(umju37.tfm) = %{tl_version}, tex(umju38.tfm) = %{tl_version}
Provides:       tex(umjuo00.tfm) = %{tl_version}, tex(umjuo01.tfm) = %{tl_version}
Provides:       tex(umjuo02.tfm) = %{tl_version}, tex(umjuo03.tfm) = %{tl_version}
Provides:       tex(umjuo04.tfm) = %{tl_version}, tex(umjuo05.tfm) = %{tl_version}
Provides:       tex(umjuo10.tfm) = %{tl_version}, tex(umjuo11.tfm) = %{tl_version}
Provides:       tex(umjuo12.tfm) = %{tl_version}, tex(umjuo13.tfm) = %{tl_version}
Provides:       tex(umjuo14.tfm) = %{tl_version}, tex(umjuo15.tfm) = %{tl_version}
Provides:       tex(umjuo16.tfm) = %{tl_version}, tex(umjuo17.tfm) = %{tl_version}
Provides:       tex(umjuo20.tfm) = %{tl_version}, tex(umjuo21.tfm) = %{tl_version}
Provides:       tex(umjuo22.tfm) = %{tl_version}, tex(umjuo23.tfm) = %{tl_version}
Provides:       tex(umjuo24.tfm) = %{tl_version}, tex(umjuo25.tfm) = %{tl_version}
Provides:       tex(umjuo26.tfm) = %{tl_version}, tex(umjuo27.tfm) = %{tl_version}
Provides:       tex(umjuo28.tfm) = %{tl_version}, tex(umjuo29.tfm) = %{tl_version}
Provides:       tex(umjuo30.tfm) = %{tl_version}, tex(umjuo31.tfm) = %{tl_version}
Provides:       tex(umjuo32.tfm) = %{tl_version}, tex(umjuo33.tfm) = %{tl_version}
Provides:       tex(umjuo34.tfm) = %{tl_version}, tex(umjuo35.tfm) = %{tl_version}
Provides:       tex(umjuo36.tfm) = %{tl_version}, tex(umjuo37.tfm) = %{tl_version}
Provides:       tex(umjuo38.tfm) = %{tl_version}, tex(umjx00.tfm) = %{tl_version}
Provides:       tex(umjx01.tfm) = %{tl_version}, tex(umjx02.tfm) = %{tl_version}
Provides:       tex(umjx03.tfm) = %{tl_version}, tex(umjx04.tfm) = %{tl_version}
Provides:       tex(umjx05.tfm) = %{tl_version}, tex(umjx10.tfm) = %{tl_version}
Provides:       tex(umjx11.tfm) = %{tl_version}, tex(umjx12.tfm) = %{tl_version}
Provides:       tex(umjx13.tfm) = %{tl_version}, tex(umjx14.tfm) = %{tl_version}
Provides:       tex(umjx15.tfm) = %{tl_version}, tex(umjx16.tfm) = %{tl_version}
Provides:       tex(umjx17.tfm) = %{tl_version}, tex(umjx20.tfm) = %{tl_version}
Provides:       tex(umjx21.tfm) = %{tl_version}, tex(umjx22.tfm) = %{tl_version}
Provides:       tex(umjx23.tfm) = %{tl_version}, tex(umjx24.tfm) = %{tl_version}
Provides:       tex(umjx25.tfm) = %{tl_version}, tex(umjx26.tfm) = %{tl_version}
Provides:       tex(umjx27.tfm) = %{tl_version}, tex(umjx28.tfm) = %{tl_version}
Provides:       tex(umjx29.tfm) = %{tl_version}, tex(umjx30.tfm) = %{tl_version}
Provides:       tex(umjx31.tfm) = %{tl_version}, tex(umjx32.tfm) = %{tl_version}
Provides:       tex(umjx33.tfm) = %{tl_version}, tex(umjx34.tfm) = %{tl_version}
Provides:       tex(umjx35.tfm) = %{tl_version}, tex(umjx36.tfm) = %{tl_version}
Provides:       tex(umjx37.tfm) = %{tl_version}, tex(umjx38.tfm) = %{tl_version}
Provides:       tex(umjxo00.tfm) = %{tl_version}, tex(umjxo01.tfm) = %{tl_version}
Provides:       tex(umjxo02.tfm) = %{tl_version}, tex(umjxo03.tfm) = %{tl_version}
Provides:       tex(umjxo04.tfm) = %{tl_version}, tex(umjxo05.tfm) = %{tl_version}
Provides:       tex(umjxo10.tfm) = %{tl_version}, tex(umjxo11.tfm) = %{tl_version}
Provides:       tex(umjxo12.tfm) = %{tl_version}, tex(umjxo13.tfm) = %{tl_version}
Provides:       tex(umjxo14.tfm) = %{tl_version}, tex(umjxo15.tfm) = %{tl_version}
Provides:       tex(umjxo16.tfm) = %{tl_version}, tex(umjxo17.tfm) = %{tl_version}
Provides:       tex(umjxo20.tfm) = %{tl_version}, tex(umjxo21.tfm) = %{tl_version}
Provides:       tex(umjxo22.tfm) = %{tl_version}, tex(umjxo23.tfm) = %{tl_version}
Provides:       tex(umjxo24.tfm) = %{tl_version}, tex(umjxo25.tfm) = %{tl_version}
Provides:       tex(umjxo26.tfm) = %{tl_version}, tex(umjxo27.tfm) = %{tl_version}
Provides:       tex(umjxo28.tfm) = %{tl_version}, tex(umjxo29.tfm) = %{tl_version}
Provides:       tex(umjxo30.tfm) = %{tl_version}, tex(umjxo31.tfm) = %{tl_version}
Provides:       tex(umjxo32.tfm) = %{tl_version}, tex(umjxo33.tfm) = %{tl_version}
Provides:       tex(umjxo34.tfm) = %{tl_version}, tex(umjxo35.tfm) = %{tl_version}
Provides:       tex(umjxo36.tfm) = %{tl_version}, tex(umjxo37.tfm) = %{tl_version}
Provides:       tex(umjxo38.tfm) = %{tl_version}, tex(uwmj00.tfm) = %{tl_version}
Provides:       tex(uwmj01.tfm) = %{tl_version}, tex(uwmj02.tfm) = %{tl_version}
Provides:       tex(uwmj03.tfm) = %{tl_version}, tex(uwmj04.tfm) = %{tl_version}
Provides:       tex(uwmj20.tfm) = %{tl_version}, tex(uwmj21.tfm) = %{tl_version}
Provides:       tex(uwmj22.tfm) = %{tl_version}, tex(uwmj23.tfm) = %{tl_version}
Provides:       tex(uwmj24.tfm) = %{tl_version}, tex(uwmj25.tfm) = %{tl_version}
Provides:       tex(uwmj26.tfm) = %{tl_version}, tex(uwmj30.tfm) = %{tl_version}
Provides:       tex(uwmj31.tfm) = %{tl_version}, tex(uwmj32.tfm) = %{tl_version}
Provides:       tex(uwmj33.tfm) = %{tl_version}, tex(uwmj4e.tfm) = %{tl_version}
Provides:       tex(uwmj4f.tfm) = %{tl_version}, tex(uwmj50.tfm) = %{tl_version}
Provides:       tex(uwmj51.tfm) = %{tl_version}, tex(uwmj52.tfm) = %{tl_version}
Provides:       tex(uwmj53.tfm) = %{tl_version}, tex(uwmj54.tfm) = %{tl_version}
Provides:       tex(uwmj55.tfm) = %{tl_version}, tex(uwmj56.tfm) = %{tl_version}
Provides:       tex(uwmj57.tfm) = %{tl_version}, tex(uwmj58.tfm) = %{tl_version}
Provides:       tex(uwmj59.tfm) = %{tl_version}, tex(uwmj5a.tfm) = %{tl_version}
Provides:       tex(uwmj5b.tfm) = %{tl_version}, tex(uwmj5c.tfm) = %{tl_version}
Provides:       tex(uwmj5d.tfm) = %{tl_version}, tex(uwmj5e.tfm) = %{tl_version}
Provides:       tex(uwmj5f.tfm) = %{tl_version}, tex(uwmj60.tfm) = %{tl_version}
Provides:       tex(uwmj61.tfm) = %{tl_version}, tex(uwmj62.tfm) = %{tl_version}
Provides:       tex(uwmj63.tfm) = %{tl_version}, tex(uwmj64.tfm) = %{tl_version}
Provides:       tex(uwmj65.tfm) = %{tl_version}, tex(uwmj66.tfm) = %{tl_version}
Provides:       tex(uwmj67.tfm) = %{tl_version}, tex(uwmj68.tfm) = %{tl_version}
Provides:       tex(uwmj69.tfm) = %{tl_version}, tex(uwmj6a.tfm) = %{tl_version}
Provides:       tex(uwmj6b.tfm) = %{tl_version}, tex(uwmj6c.tfm) = %{tl_version}
Provides:       tex(uwmj6d.tfm) = %{tl_version}, tex(uwmj6e.tfm) = %{tl_version}
Provides:       tex(uwmj6f.tfm) = %{tl_version}, tex(uwmj70.tfm) = %{tl_version}
Provides:       tex(uwmj71.tfm) = %{tl_version}, tex(uwmj72.tfm) = %{tl_version}
Provides:       tex(uwmj73.tfm) = %{tl_version}, tex(uwmj74.tfm) = %{tl_version}
Provides:       tex(uwmj75.tfm) = %{tl_version}, tex(uwmj76.tfm) = %{tl_version}
Provides:       tex(uwmj77.tfm) = %{tl_version}, tex(uwmj78.tfm) = %{tl_version}
Provides:       tex(uwmj79.tfm) = %{tl_version}, tex(uwmj7a.tfm) = %{tl_version}
Provides:       tex(uwmj7b.tfm) = %{tl_version}, tex(uwmj7c.tfm) = %{tl_version}
Provides:       tex(uwmj7d.tfm) = %{tl_version}, tex(uwmj7e.tfm) = %{tl_version}
Provides:       tex(uwmj7f.tfm) = %{tl_version}, tex(uwmj80.tfm) = %{tl_version}
Provides:       tex(uwmj81.tfm) = %{tl_version}, tex(uwmj82.tfm) = %{tl_version}
Provides:       tex(uwmj83.tfm) = %{tl_version}, tex(uwmj84.tfm) = %{tl_version}
Provides:       tex(uwmj85.tfm) = %{tl_version}, tex(uwmj86.tfm) = %{tl_version}
Provides:       tex(uwmj87.tfm) = %{tl_version}, tex(uwmj88.tfm) = %{tl_version}
Provides:       tex(uwmj89.tfm) = %{tl_version}, tex(uwmj8a.tfm) = %{tl_version}
Provides:       tex(uwmj8b.tfm) = %{tl_version}, tex(uwmj8c.tfm) = %{tl_version}
Provides:       tex(uwmj8d.tfm) = %{tl_version}, tex(uwmj8e.tfm) = %{tl_version}
Provides:       tex(uwmj8f.tfm) = %{tl_version}, tex(uwmj90.tfm) = %{tl_version}
Provides:       tex(uwmj91.tfm) = %{tl_version}, tex(uwmj92.tfm) = %{tl_version}
Provides:       tex(uwmj93.tfm) = %{tl_version}, tex(uwmj94.tfm) = %{tl_version}
Provides:       tex(uwmj95.tfm) = %{tl_version}, tex(uwmj96.tfm) = %{tl_version}
Provides:       tex(uwmj97.tfm) = %{tl_version}, tex(uwmj98.tfm) = %{tl_version}
Provides:       tex(uwmj99.tfm) = %{tl_version}, tex(uwmj9a.tfm) = %{tl_version}
Provides:       tex(uwmj9b.tfm) = %{tl_version}, tex(uwmj9c.tfm) = %{tl_version}
Provides:       tex(uwmj9d.tfm) = %{tl_version}, tex(uwmj9e.tfm) = %{tl_version}
Provides:       tex(uwmj9f.tfm) = %{tl_version}, tex(uwmjac.tfm) = %{tl_version}
Provides:       tex(uwmjad.tfm) = %{tl_version}, tex(uwmjae.tfm) = %{tl_version}
Provides:       tex(uwmjaf.tfm) = %{tl_version}, tex(uwmjb0.tfm) = %{tl_version}
Provides:       tex(uwmjb1.tfm) = %{tl_version}, tex(uwmjb2.tfm) = %{tl_version}
Provides:       tex(uwmjb3.tfm) = %{tl_version}, tex(uwmjb4.tfm) = %{tl_version}
Provides:       tex(uwmjb5.tfm) = %{tl_version}, tex(uwmjb6.tfm) = %{tl_version}
Provides:       tex(uwmjb7.tfm) = %{tl_version}, tex(uwmjb8.tfm) = %{tl_version}
Provides:       tex(uwmjb9.tfm) = %{tl_version}, tex(uwmjba.tfm) = %{tl_version}
Provides:       tex(uwmjbb.tfm) = %{tl_version}, tex(uwmjbc.tfm) = %{tl_version}
Provides:       tex(uwmjbd.tfm) = %{tl_version}, tex(uwmjbe.tfm) = %{tl_version}
Provides:       tex(uwmjbf.tfm) = %{tl_version}, tex(uwmjc0.tfm) = %{tl_version}
Provides:       tex(uwmjc00.tfm) = %{tl_version}, tex(uwmjc01.tfm) = %{tl_version}
Provides:       tex(uwmjc02.tfm) = %{tl_version}, tex(uwmjc03.tfm) = %{tl_version}
Provides:       tex(uwmjc04.tfm) = %{tl_version}, tex(uwmjc1.tfm) = %{tl_version}
Provides:       tex(uwmjc2.tfm) = %{tl_version}, tex(uwmjc20.tfm) = %{tl_version}
Provides:       tex(uwmjc21.tfm) = %{tl_version}, tex(uwmjc22.tfm) = %{tl_version}
Provides:       tex(uwmjc23.tfm) = %{tl_version}, tex(uwmjc24.tfm) = %{tl_version}
Provides:       tex(uwmjc25.tfm) = %{tl_version}, tex(uwmjc26.tfm) = %{tl_version}
Provides:       tex(uwmjc3.tfm) = %{tl_version}, tex(uwmjc30.tfm) = %{tl_version}
Provides:       tex(uwmjc31.tfm) = %{tl_version}, tex(uwmjc32.tfm) = %{tl_version}
Provides:       tex(uwmjc33.tfm) = %{tl_version}, tex(uwmjc4.tfm) = %{tl_version}
Provides:       tex(uwmjc4e.tfm) = %{tl_version}, tex(uwmjc4f.tfm) = %{tl_version}
Provides:       tex(uwmjc5.tfm) = %{tl_version}, tex(uwmjc50.tfm) = %{tl_version}
Provides:       tex(uwmjc51.tfm) = %{tl_version}, tex(uwmjc52.tfm) = %{tl_version}
Provides:       tex(uwmjc53.tfm) = %{tl_version}, tex(uwmjc54.tfm) = %{tl_version}
Provides:       tex(uwmjc55.tfm) = %{tl_version}, tex(uwmjc56.tfm) = %{tl_version}
Provides:       tex(uwmjc57.tfm) = %{tl_version}, tex(uwmjc58.tfm) = %{tl_version}
Provides:       tex(uwmjc59.tfm) = %{tl_version}, tex(uwmjc5a.tfm) = %{tl_version}
Provides:       tex(uwmjc5b.tfm) = %{tl_version}, tex(uwmjc5c.tfm) = %{tl_version}
Provides:       tex(uwmjc5d.tfm) = %{tl_version}, tex(uwmjc5e.tfm) = %{tl_version}
Provides:       tex(uwmjc5f.tfm) = %{tl_version}, tex(uwmjc6.tfm) = %{tl_version}
Provides:       tex(uwmjc60.tfm) = %{tl_version}, tex(uwmjc61.tfm) = %{tl_version}
Provides:       tex(uwmjc62.tfm) = %{tl_version}, tex(uwmjc63.tfm) = %{tl_version}
Provides:       tex(uwmjc64.tfm) = %{tl_version}, tex(uwmjc65.tfm) = %{tl_version}
Provides:       tex(uwmjc66.tfm) = %{tl_version}, tex(uwmjc67.tfm) = %{tl_version}
Provides:       tex(uwmjc68.tfm) = %{tl_version}, tex(uwmjc69.tfm) = %{tl_version}
Provides:       tex(uwmjc6a.tfm) = %{tl_version}, tex(uwmjc6b.tfm) = %{tl_version}
Provides:       tex(uwmjc6c.tfm) = %{tl_version}, tex(uwmjc6d.tfm) = %{tl_version}
Provides:       tex(uwmjc6e.tfm) = %{tl_version}, tex(uwmjc6f.tfm) = %{tl_version}
Provides:       tex(uwmjc7.tfm) = %{tl_version}, tex(uwmjc70.tfm) = %{tl_version}
Provides:       tex(uwmjc71.tfm) = %{tl_version}, tex(uwmjc72.tfm) = %{tl_version}
Provides:       tex(uwmjc73.tfm) = %{tl_version}, tex(uwmjc74.tfm) = %{tl_version}
Provides:       tex(uwmjc75.tfm) = %{tl_version}, tex(uwmjc76.tfm) = %{tl_version}
Provides:       tex(uwmjc77.tfm) = %{tl_version}, tex(uwmjc78.tfm) = %{tl_version}
Provides:       tex(uwmjc79.tfm) = %{tl_version}, tex(uwmjc7a.tfm) = %{tl_version}
Provides:       tex(uwmjc7b.tfm) = %{tl_version}, tex(uwmjc7c.tfm) = %{tl_version}
Provides:       tex(uwmjc7d.tfm) = %{tl_version}, tex(uwmjc7e.tfm) = %{tl_version}
Provides:       tex(uwmjc7f.tfm) = %{tl_version}, tex(uwmjc8.tfm) = %{tl_version}
Provides:       tex(uwmjc80.tfm) = %{tl_version}, tex(uwmjc81.tfm) = %{tl_version}
Provides:       tex(uwmjc82.tfm) = %{tl_version}, tex(uwmjc83.tfm) = %{tl_version}
Provides:       tex(uwmjc84.tfm) = %{tl_version}, tex(uwmjc85.tfm) = %{tl_version}
Provides:       tex(uwmjc86.tfm) = %{tl_version}, tex(uwmjc87.tfm) = %{tl_version}
Provides:       tex(uwmjc88.tfm) = %{tl_version}, tex(uwmjc89.tfm) = %{tl_version}
Provides:       tex(uwmjc8a.tfm) = %{tl_version}, tex(uwmjc8b.tfm) = %{tl_version}
Provides:       tex(uwmjc8c.tfm) = %{tl_version}, tex(uwmjc8d.tfm) = %{tl_version}
Provides:       tex(uwmjc8e.tfm) = %{tl_version}, tex(uwmjc8f.tfm) = %{tl_version}
Provides:       tex(uwmjc9.tfm) = %{tl_version}, tex(uwmjc90.tfm) = %{tl_version}
Provides:       tex(uwmjc91.tfm) = %{tl_version}, tex(uwmjc92.tfm) = %{tl_version}
Provides:       tex(uwmjc93.tfm) = %{tl_version}, tex(uwmjc94.tfm) = %{tl_version}
Provides:       tex(uwmjc95.tfm) = %{tl_version}, tex(uwmjc96.tfm) = %{tl_version}
Provides:       tex(uwmjc97.tfm) = %{tl_version}, tex(uwmjc98.tfm) = %{tl_version}
Provides:       tex(uwmjc99.tfm) = %{tl_version}, tex(uwmjc9a.tfm) = %{tl_version}
Provides:       tex(uwmjc9b.tfm) = %{tl_version}, tex(uwmjc9c.tfm) = %{tl_version}
Provides:       tex(uwmjc9d.tfm) = %{tl_version}, tex(uwmjc9e.tfm) = %{tl_version}
Provides:       tex(uwmjc9f.tfm) = %{tl_version}, tex(uwmjca.tfm) = %{tl_version}
Provides:       tex(uwmjcac.tfm) = %{tl_version}, tex(uwmjcad.tfm) = %{tl_version}
Provides:       tex(uwmjcae.tfm) = %{tl_version}, tex(uwmjcaf.tfm) = %{tl_version}
Provides:       tex(uwmjcb.tfm) = %{tl_version}, tex(uwmjcb0.tfm) = %{tl_version}
Provides:       tex(uwmjcb1.tfm) = %{tl_version}, tex(uwmjcb2.tfm) = %{tl_version}
Provides:       tex(uwmjcb3.tfm) = %{tl_version}, tex(uwmjcb4.tfm) = %{tl_version}
Provides:       tex(uwmjcb5.tfm) = %{tl_version}, tex(uwmjcb6.tfm) = %{tl_version}
Provides:       tex(uwmjcb7.tfm) = %{tl_version}, tex(uwmjcb8.tfm) = %{tl_version}
Provides:       tex(uwmjcb9.tfm) = %{tl_version}, tex(uwmjcba.tfm) = %{tl_version}
Provides:       tex(uwmjcbb.tfm) = %{tl_version}, tex(uwmjcbc.tfm) = %{tl_version}
Provides:       tex(uwmjcbd.tfm) = %{tl_version}, tex(uwmjcbe.tfm) = %{tl_version}
Provides:       tex(uwmjcbf.tfm) = %{tl_version}, tex(uwmjcc.tfm) = %{tl_version}
Provides:       tex(uwmjcc0.tfm) = %{tl_version}, tex(uwmjcc1.tfm) = %{tl_version}
Provides:       tex(uwmjcc2.tfm) = %{tl_version}, tex(uwmjcc3.tfm) = %{tl_version}
Provides:       tex(uwmjcc4.tfm) = %{tl_version}, tex(uwmjcc5.tfm) = %{tl_version}
Provides:       tex(uwmjcc6.tfm) = %{tl_version}, tex(uwmjcc7.tfm) = %{tl_version}
Provides:       tex(uwmjcc8.tfm) = %{tl_version}, tex(uwmjcc9.tfm) = %{tl_version}
Provides:       tex(uwmjcca.tfm) = %{tl_version}, tex(uwmjccb.tfm) = %{tl_version}
Provides:       tex(uwmjccc.tfm) = %{tl_version}, tex(uwmjccd.tfm) = %{tl_version}
Provides:       tex(uwmjcce.tfm) = %{tl_version}, tex(uwmjccf.tfm) = %{tl_version}
Provides:       tex(uwmjcd.tfm) = %{tl_version}, tex(uwmjcd0.tfm) = %{tl_version}
Provides:       tex(uwmjcd1.tfm) = %{tl_version}, tex(uwmjcd2.tfm) = %{tl_version}
Provides:       tex(uwmjcd3.tfm) = %{tl_version}, tex(uwmjcd4.tfm) = %{tl_version}
Provides:       tex(uwmjcd5.tfm) = %{tl_version}, tex(uwmjcd6.tfm) = %{tl_version}
Provides:       tex(uwmjcd7.tfm) = %{tl_version}, tex(uwmjce.tfm) = %{tl_version}
Provides:       tex(uwmjcf.tfm) = %{tl_version}, tex(uwmjcf9.tfm) = %{tl_version}
Provides:       tex(uwmjcfa.tfm) = %{tl_version}, tex(uwmjcff.tfm) = %{tl_version}
Provides:       tex(uwmjco00.tfm) = %{tl_version}, tex(uwmjco01.tfm) = %{tl_version}
Provides:       tex(uwmjco02.tfm) = %{tl_version}, tex(uwmjco03.tfm) = %{tl_version}
Provides:       tex(uwmjco04.tfm) = %{tl_version}, tex(uwmjco20.tfm) = %{tl_version}
Provides:       tex(uwmjco21.tfm) = %{tl_version}, tex(uwmjco22.tfm) = %{tl_version}
Provides:       tex(uwmjco23.tfm) = %{tl_version}, tex(uwmjco24.tfm) = %{tl_version}
Provides:       tex(uwmjco25.tfm) = %{tl_version}, tex(uwmjco26.tfm) = %{tl_version}
Provides:       tex(uwmjco30.tfm) = %{tl_version}, tex(uwmjco31.tfm) = %{tl_version}
Provides:       tex(uwmjco32.tfm) = %{tl_version}, tex(uwmjco33.tfm) = %{tl_version}
Provides:       tex(uwmjco4e.tfm) = %{tl_version}, tex(uwmjco4f.tfm) = %{tl_version}
Provides:       tex(uwmjco50.tfm) = %{tl_version}, tex(uwmjco51.tfm) = %{tl_version}
Provides:       tex(uwmjco52.tfm) = %{tl_version}, tex(uwmjco53.tfm) = %{tl_version}
Provides:       tex(uwmjco54.tfm) = %{tl_version}, tex(uwmjco55.tfm) = %{tl_version}
Provides:       tex(uwmjco56.tfm) = %{tl_version}, tex(uwmjco57.tfm) = %{tl_version}
Provides:       tex(uwmjco58.tfm) = %{tl_version}, tex(uwmjco59.tfm) = %{tl_version}
Provides:       tex(uwmjco5a.tfm) = %{tl_version}, tex(uwmjco5b.tfm) = %{tl_version}
Provides:       tex(uwmjco5c.tfm) = %{tl_version}, tex(uwmjco5d.tfm) = %{tl_version}
Provides:       tex(uwmjco5e.tfm) = %{tl_version}, tex(uwmjco5f.tfm) = %{tl_version}
Provides:       tex(uwmjco60.tfm) = %{tl_version}, tex(uwmjco61.tfm) = %{tl_version}
Provides:       tex(uwmjco62.tfm) = %{tl_version}, tex(uwmjco63.tfm) = %{tl_version}
Provides:       tex(uwmjco64.tfm) = %{tl_version}, tex(uwmjco65.tfm) = %{tl_version}
Provides:       tex(uwmjco66.tfm) = %{tl_version}, tex(uwmjco67.tfm) = %{tl_version}
Provides:       tex(uwmjco68.tfm) = %{tl_version}, tex(uwmjco69.tfm) = %{tl_version}
Provides:       tex(uwmjco6a.tfm) = %{tl_version}, tex(uwmjco6b.tfm) = %{tl_version}
Provides:       tex(uwmjco6c.tfm) = %{tl_version}, tex(uwmjco6d.tfm) = %{tl_version}
Provides:       tex(uwmjco6e.tfm) = %{tl_version}, tex(uwmjco6f.tfm) = %{tl_version}
Provides:       tex(uwmjco70.tfm) = %{tl_version}, tex(uwmjco71.tfm) = %{tl_version}
Provides:       tex(uwmjco72.tfm) = %{tl_version}, tex(uwmjco73.tfm) = %{tl_version}
Provides:       tex(uwmjco74.tfm) = %{tl_version}, tex(uwmjco75.tfm) = %{tl_version}
Provides:       tex(uwmjco76.tfm) = %{tl_version}, tex(uwmjco77.tfm) = %{tl_version}
Provides:       tex(uwmjco78.tfm) = %{tl_version}, tex(uwmjco79.tfm) = %{tl_version}
Provides:       tex(uwmjco7a.tfm) = %{tl_version}, tex(uwmjco7b.tfm) = %{tl_version}
Provides:       tex(uwmjco7c.tfm) = %{tl_version}, tex(uwmjco7d.tfm) = %{tl_version}
Provides:       tex(uwmjco7e.tfm) = %{tl_version}, tex(uwmjco7f.tfm) = %{tl_version}
Provides:       tex(uwmjco80.tfm) = %{tl_version}, tex(uwmjco81.tfm) = %{tl_version}
Provides:       tex(uwmjco82.tfm) = %{tl_version}, tex(uwmjco83.tfm) = %{tl_version}
Provides:       tex(uwmjco84.tfm) = %{tl_version}, tex(uwmjco85.tfm) = %{tl_version}
Provides:       tex(uwmjco86.tfm) = %{tl_version}, tex(uwmjco87.tfm) = %{tl_version}
Provides:       tex(uwmjco88.tfm) = %{tl_version}, tex(uwmjco89.tfm) = %{tl_version}
Provides:       tex(uwmjco8a.tfm) = %{tl_version}, tex(uwmjco8b.tfm) = %{tl_version}
Provides:       tex(uwmjco8c.tfm) = %{tl_version}, tex(uwmjco8d.tfm) = %{tl_version}
Provides:       tex(uwmjco8e.tfm) = %{tl_version}, tex(uwmjco8f.tfm) = %{tl_version}
Provides:       tex(uwmjco90.tfm) = %{tl_version}, tex(uwmjco91.tfm) = %{tl_version}
Provides:       tex(uwmjco92.tfm) = %{tl_version}, tex(uwmjco93.tfm) = %{tl_version}
Provides:       tex(uwmjco94.tfm) = %{tl_version}, tex(uwmjco95.tfm) = %{tl_version}
Provides:       tex(uwmjco96.tfm) = %{tl_version}, tex(uwmjco97.tfm) = %{tl_version}
Provides:       tex(uwmjco98.tfm) = %{tl_version}, tex(uwmjco99.tfm) = %{tl_version}
Provides:       tex(uwmjco9a.tfm) = %{tl_version}, tex(uwmjco9b.tfm) = %{tl_version}
Provides:       tex(uwmjco9c.tfm) = %{tl_version}, tex(uwmjco9d.tfm) = %{tl_version}
Provides:       tex(uwmjco9e.tfm) = %{tl_version}, tex(uwmjco9f.tfm) = %{tl_version}
Provides:       tex(uwmjcoac.tfm) = %{tl_version}, tex(uwmjcoad.tfm) = %{tl_version}
Provides:       tex(uwmjcoae.tfm) = %{tl_version}, tex(uwmjcoaf.tfm) = %{tl_version}
Provides:       tex(uwmjcob0.tfm) = %{tl_version}, tex(uwmjcob1.tfm) = %{tl_version}
Provides:       tex(uwmjcob2.tfm) = %{tl_version}, tex(uwmjcob3.tfm) = %{tl_version}
Provides:       tex(uwmjcob4.tfm) = %{tl_version}, tex(uwmjcob5.tfm) = %{tl_version}
Provides:       tex(uwmjcob6.tfm) = %{tl_version}, tex(uwmjcob7.tfm) = %{tl_version}
Provides:       tex(uwmjcob8.tfm) = %{tl_version}, tex(uwmjcob9.tfm) = %{tl_version}
Provides:       tex(uwmjcoba.tfm) = %{tl_version}, tex(uwmjcobb.tfm) = %{tl_version}
Provides:       tex(uwmjcobc.tfm) = %{tl_version}, tex(uwmjcobd.tfm) = %{tl_version}
Provides:       tex(uwmjcobe.tfm) = %{tl_version}, tex(uwmjcobf.tfm) = %{tl_version}
Provides:       tex(uwmjcoc0.tfm) = %{tl_version}, tex(uwmjcoc1.tfm) = %{tl_version}
Provides:       tex(uwmjcoc2.tfm) = %{tl_version}, tex(uwmjcoc3.tfm) = %{tl_version}
Provides:       tex(uwmjcoc4.tfm) = %{tl_version}, tex(uwmjcoc5.tfm) = %{tl_version}
Provides:       tex(uwmjcoc6.tfm) = %{tl_version}, tex(uwmjcoc7.tfm) = %{tl_version}
Provides:       tex(uwmjcoc8.tfm) = %{tl_version}, tex(uwmjcoc9.tfm) = %{tl_version}
Provides:       tex(uwmjcoca.tfm) = %{tl_version}, tex(uwmjcocb.tfm) = %{tl_version}
Provides:       tex(uwmjcocc.tfm) = %{tl_version}, tex(uwmjcocd.tfm) = %{tl_version}
Provides:       tex(uwmjcoce.tfm) = %{tl_version}, tex(uwmjcocf.tfm) = %{tl_version}
Provides:       tex(uwmjcod0.tfm) = %{tl_version}, tex(uwmjcod1.tfm) = %{tl_version}
Provides:       tex(uwmjcod2.tfm) = %{tl_version}, tex(uwmjcod3.tfm) = %{tl_version}
Provides:       tex(uwmjcod4.tfm) = %{tl_version}, tex(uwmjcod5.tfm) = %{tl_version}
Provides:       tex(uwmjcod6.tfm) = %{tl_version}, tex(uwmjcod7.tfm) = %{tl_version}
Provides:       tex(uwmjcof9.tfm) = %{tl_version}, tex(uwmjcofa.tfm) = %{tl_version}
Provides:       tex(uwmjcoff.tfm) = %{tl_version}, tex(uwmjd0.tfm) = %{tl_version}
Provides:       tex(uwmjd1.tfm) = %{tl_version}, tex(uwmjd2.tfm) = %{tl_version}
Provides:       tex(uwmjd3.tfm) = %{tl_version}, tex(uwmjd4.tfm) = %{tl_version}
Provides:       tex(uwmjd5.tfm) = %{tl_version}, tex(uwmjd6.tfm) = %{tl_version}
Provides:       tex(uwmjd7.tfm) = %{tl_version}, tex(uwmjf9.tfm) = %{tl_version}
Provides:       tex(uwmjfa.tfm) = %{tl_version}, tex(uwmjff.tfm) = %{tl_version}
Provides:       tex(uwmjo00.tfm) = %{tl_version}, tex(uwmjo01.tfm) = %{tl_version}
Provides:       tex(uwmjo02.tfm) = %{tl_version}, tex(uwmjo03.tfm) = %{tl_version}
Provides:       tex(uwmjo04.tfm) = %{tl_version}, tex(uwmjo20.tfm) = %{tl_version}
Provides:       tex(uwmjo21.tfm) = %{tl_version}, tex(uwmjo22.tfm) = %{tl_version}
Provides:       tex(uwmjo23.tfm) = %{tl_version}, tex(uwmjo24.tfm) = %{tl_version}
Provides:       tex(uwmjo25.tfm) = %{tl_version}, tex(uwmjo26.tfm) = %{tl_version}
Provides:       tex(uwmjo30.tfm) = %{tl_version}, tex(uwmjo31.tfm) = %{tl_version}
Provides:       tex(uwmjo32.tfm) = %{tl_version}, tex(uwmjo33.tfm) = %{tl_version}
Provides:       tex(uwmjo4e.tfm) = %{tl_version}, tex(uwmjo4f.tfm) = %{tl_version}
Provides:       tex(uwmjo50.tfm) = %{tl_version}, tex(uwmjo51.tfm) = %{tl_version}
Provides:       tex(uwmjo52.tfm) = %{tl_version}, tex(uwmjo53.tfm) = %{tl_version}
Provides:       tex(uwmjo54.tfm) = %{tl_version}, tex(uwmjo55.tfm) = %{tl_version}
Provides:       tex(uwmjo56.tfm) = %{tl_version}, tex(uwmjo57.tfm) = %{tl_version}
Provides:       tex(uwmjo58.tfm) = %{tl_version}, tex(uwmjo59.tfm) = %{tl_version}
Provides:       tex(uwmjo5a.tfm) = %{tl_version}, tex(uwmjo5b.tfm) = %{tl_version}
Provides:       tex(uwmjo5c.tfm) = %{tl_version}, tex(uwmjo5d.tfm) = %{tl_version}
Provides:       tex(uwmjo5e.tfm) = %{tl_version}, tex(uwmjo5f.tfm) = %{tl_version}
Provides:       tex(uwmjo60.tfm) = %{tl_version}, tex(uwmjo61.tfm) = %{tl_version}
Provides:       tex(uwmjo62.tfm) = %{tl_version}, tex(uwmjo63.tfm) = %{tl_version}
Provides:       tex(uwmjo64.tfm) = %{tl_version}, tex(uwmjo65.tfm) = %{tl_version}
Provides:       tex(uwmjo66.tfm) = %{tl_version}, tex(uwmjo67.tfm) = %{tl_version}
Provides:       tex(uwmjo68.tfm) = %{tl_version}, tex(uwmjo69.tfm) = %{tl_version}
Provides:       tex(uwmjo6a.tfm) = %{tl_version}, tex(uwmjo6b.tfm) = %{tl_version}
Provides:       tex(uwmjo6c.tfm) = %{tl_version}, tex(uwmjo6d.tfm) = %{tl_version}
Provides:       tex(uwmjo6e.tfm) = %{tl_version}, tex(uwmjo6f.tfm) = %{tl_version}
Provides:       tex(uwmjo70.tfm) = %{tl_version}, tex(uwmjo71.tfm) = %{tl_version}
Provides:       tex(uwmjo72.tfm) = %{tl_version}, tex(uwmjo73.tfm) = %{tl_version}
Provides:       tex(uwmjo74.tfm) = %{tl_version}, tex(uwmjo75.tfm) = %{tl_version}
Provides:       tex(uwmjo76.tfm) = %{tl_version}, tex(uwmjo77.tfm) = %{tl_version}
Provides:       tex(uwmjo78.tfm) = %{tl_version}, tex(uwmjo79.tfm) = %{tl_version}
Provides:       tex(uwmjo7a.tfm) = %{tl_version}, tex(uwmjo7b.tfm) = %{tl_version}
Provides:       tex(uwmjo7c.tfm) = %{tl_version}, tex(uwmjo7d.tfm) = %{tl_version}
Provides:       tex(uwmjo7e.tfm) = %{tl_version}, tex(uwmjo7f.tfm) = %{tl_version}
Provides:       tex(uwmjo80.tfm) = %{tl_version}, tex(uwmjo81.tfm) = %{tl_version}
Provides:       tex(uwmjo82.tfm) = %{tl_version}, tex(uwmjo83.tfm) = %{tl_version}
Provides:       tex(uwmjo84.tfm) = %{tl_version}, tex(uwmjo85.tfm) = %{tl_version}
Provides:       tex(uwmjo86.tfm) = %{tl_version}, tex(uwmjo87.tfm) = %{tl_version}
Provides:       tex(uwmjo88.tfm) = %{tl_version}, tex(uwmjo89.tfm) = %{tl_version}
Provides:       tex(uwmjo8a.tfm) = %{tl_version}, tex(uwmjo8b.tfm) = %{tl_version}
Provides:       tex(uwmjo8c.tfm) = %{tl_version}, tex(uwmjo8d.tfm) = %{tl_version}
Provides:       tex(uwmjo8e.tfm) = %{tl_version}, tex(uwmjo8f.tfm) = %{tl_version}
Provides:       tex(uwmjo90.tfm) = %{tl_version}, tex(uwmjo91.tfm) = %{tl_version}
Provides:       tex(uwmjo92.tfm) = %{tl_version}, tex(uwmjo93.tfm) = %{tl_version}
Provides:       tex(uwmjo94.tfm) = %{tl_version}, tex(uwmjo95.tfm) = %{tl_version}
Provides:       tex(uwmjo96.tfm) = %{tl_version}, tex(uwmjo97.tfm) = %{tl_version}
Provides:       tex(uwmjo98.tfm) = %{tl_version}, tex(uwmjo99.tfm) = %{tl_version}
Provides:       tex(uwmjo9a.tfm) = %{tl_version}, tex(uwmjo9b.tfm) = %{tl_version}
Provides:       tex(uwmjo9c.tfm) = %{tl_version}, tex(uwmjo9d.tfm) = %{tl_version}
Provides:       tex(uwmjo9e.tfm) = %{tl_version}, tex(uwmjo9f.tfm) = %{tl_version}
Provides:       tex(uwmjoac.tfm) = %{tl_version}, tex(uwmjoad.tfm) = %{tl_version}
Provides:       tex(uwmjoae.tfm) = %{tl_version}, tex(uwmjoaf.tfm) = %{tl_version}
Provides:       tex(uwmjob0.tfm) = %{tl_version}, tex(uwmjob1.tfm) = %{tl_version}
Provides:       tex(uwmjob2.tfm) = %{tl_version}, tex(uwmjob3.tfm) = %{tl_version}
Provides:       tex(uwmjob4.tfm) = %{tl_version}, tex(uwmjob5.tfm) = %{tl_version}
Provides:       tex(uwmjob6.tfm) = %{tl_version}, tex(uwmjob7.tfm) = %{tl_version}
Provides:       tex(uwmjob8.tfm) = %{tl_version}, tex(uwmjob9.tfm) = %{tl_version}
Provides:       tex(uwmjoba.tfm) = %{tl_version}, tex(uwmjobb.tfm) = %{tl_version}
Provides:       tex(uwmjobc.tfm) = %{tl_version}, tex(uwmjobd.tfm) = %{tl_version}
Provides:       tex(uwmjobe.tfm) = %{tl_version}, tex(uwmjobf.tfm) = %{tl_version}
Provides:       tex(uwmjoc0.tfm) = %{tl_version}, tex(uwmjoc1.tfm) = %{tl_version}
Provides:       tex(uwmjoc2.tfm) = %{tl_version}, tex(uwmjoc3.tfm) = %{tl_version}
Provides:       tex(uwmjoc4.tfm) = %{tl_version}, tex(uwmjoc5.tfm) = %{tl_version}
Provides:       tex(uwmjoc6.tfm) = %{tl_version}, tex(uwmjoc7.tfm) = %{tl_version}
Provides:       tex(uwmjoc8.tfm) = %{tl_version}, tex(uwmjoc9.tfm) = %{tl_version}
Provides:       tex(uwmjoca.tfm) = %{tl_version}, tex(uwmjocb.tfm) = %{tl_version}
Provides:       tex(uwmjocc.tfm) = %{tl_version}, tex(uwmjocd.tfm) = %{tl_version}
Provides:       tex(uwmjoce.tfm) = %{tl_version}, tex(uwmjocf.tfm) = %{tl_version}
Provides:       tex(uwmjod0.tfm) = %{tl_version}, tex(uwmjod1.tfm) = %{tl_version}
Provides:       tex(uwmjod2.tfm) = %{tl_version}, tex(uwmjod3.tfm) = %{tl_version}
Provides:       tex(uwmjod4.tfm) = %{tl_version}, tex(uwmjod5.tfm) = %{tl_version}
Provides:       tex(uwmjod6.tfm) = %{tl_version}, tex(uwmjod7.tfm) = %{tl_version}
Provides:       tex(uwmjof9.tfm) = %{tl_version}, tex(uwmjofa.tfm) = %{tl_version}
Provides:       tex(uwmjoff.tfm) = %{tl_version}, tex(uwmju00.tfm) = %{tl_version}
Provides:       tex(uwmju01.tfm) = %{tl_version}, tex(uwmju02.tfm) = %{tl_version}
Provides:       tex(uwmju03.tfm) = %{tl_version}, tex(uwmju04.tfm) = %{tl_version}
Provides:       tex(uwmju20.tfm) = %{tl_version}, tex(uwmju21.tfm) = %{tl_version}
Provides:       tex(uwmju22.tfm) = %{tl_version}, tex(uwmju23.tfm) = %{tl_version}
Provides:       tex(uwmju24.tfm) = %{tl_version}, tex(uwmju25.tfm) = %{tl_version}
Provides:       tex(uwmju26.tfm) = %{tl_version}, tex(uwmju30.tfm) = %{tl_version}
Provides:       tex(uwmju31.tfm) = %{tl_version}, tex(uwmju32.tfm) = %{tl_version}
Provides:       tex(uwmju33.tfm) = %{tl_version}, tex(uwmju4e.tfm) = %{tl_version}
Provides:       tex(uwmju4f.tfm) = %{tl_version}, tex(uwmju50.tfm) = %{tl_version}
Provides:       tex(uwmju51.tfm) = %{tl_version}, tex(uwmju52.tfm) = %{tl_version}
Provides:       tex(uwmju53.tfm) = %{tl_version}, tex(uwmju54.tfm) = %{tl_version}
Provides:       tex(uwmju55.tfm) = %{tl_version}, tex(uwmju56.tfm) = %{tl_version}
Provides:       tex(uwmju57.tfm) = %{tl_version}, tex(uwmju58.tfm) = %{tl_version}
Provides:       tex(uwmju59.tfm) = %{tl_version}, tex(uwmju5a.tfm) = %{tl_version}
Provides:       tex(uwmju5b.tfm) = %{tl_version}, tex(uwmju5c.tfm) = %{tl_version}
Provides:       tex(uwmju5d.tfm) = %{tl_version}, tex(uwmju5e.tfm) = %{tl_version}
Provides:       tex(uwmju5f.tfm) = %{tl_version}, tex(uwmju60.tfm) = %{tl_version}
Provides:       tex(uwmju61.tfm) = %{tl_version}, tex(uwmju62.tfm) = %{tl_version}
Provides:       tex(uwmju63.tfm) = %{tl_version}, tex(uwmju64.tfm) = %{tl_version}
Provides:       tex(uwmju65.tfm) = %{tl_version}, tex(uwmju66.tfm) = %{tl_version}
Provides:       tex(uwmju67.tfm) = %{tl_version}, tex(uwmju68.tfm) = %{tl_version}
Provides:       tex(uwmju69.tfm) = %{tl_version}, tex(uwmju6a.tfm) = %{tl_version}
Provides:       tex(uwmju6b.tfm) = %{tl_version}, tex(uwmju6c.tfm) = %{tl_version}
Provides:       tex(uwmju6d.tfm) = %{tl_version}, tex(uwmju6e.tfm) = %{tl_version}
Provides:       tex(uwmju6f.tfm) = %{tl_version}, tex(uwmju70.tfm) = %{tl_version}
Provides:       tex(uwmju71.tfm) = %{tl_version}, tex(uwmju72.tfm) = %{tl_version}
Provides:       tex(uwmju73.tfm) = %{tl_version}, tex(uwmju74.tfm) = %{tl_version}
Provides:       tex(uwmju75.tfm) = %{tl_version}, tex(uwmju76.tfm) = %{tl_version}
Provides:       tex(uwmju77.tfm) = %{tl_version}, tex(uwmju78.tfm) = %{tl_version}
Provides:       tex(uwmju79.tfm) = %{tl_version}, tex(uwmju7a.tfm) = %{tl_version}
Provides:       tex(uwmju7b.tfm) = %{tl_version}, tex(uwmju7c.tfm) = %{tl_version}
Provides:       tex(uwmju7d.tfm) = %{tl_version}, tex(uwmju7e.tfm) = %{tl_version}
Provides:       tex(uwmju7f.tfm) = %{tl_version}, tex(uwmju80.tfm) = %{tl_version}
Provides:       tex(uwmju81.tfm) = %{tl_version}, tex(uwmju82.tfm) = %{tl_version}
Provides:       tex(uwmju83.tfm) = %{tl_version}, tex(uwmju84.tfm) = %{tl_version}
Provides:       tex(uwmju85.tfm) = %{tl_version}, tex(uwmju86.tfm) = %{tl_version}
Provides:       tex(uwmju87.tfm) = %{tl_version}, tex(uwmju88.tfm) = %{tl_version}
Provides:       tex(uwmju89.tfm) = %{tl_version}, tex(uwmju8a.tfm) = %{tl_version}
Provides:       tex(uwmju8b.tfm) = %{tl_version}, tex(uwmju8c.tfm) = %{tl_version}
Provides:       tex(uwmju8d.tfm) = %{tl_version}, tex(uwmju8e.tfm) = %{tl_version}
Provides:       tex(uwmju8f.tfm) = %{tl_version}, tex(uwmju90.tfm) = %{tl_version}
Provides:       tex(uwmju91.tfm) = %{tl_version}, tex(uwmju92.tfm) = %{tl_version}
Provides:       tex(uwmju93.tfm) = %{tl_version}, tex(uwmju94.tfm) = %{tl_version}
Provides:       tex(uwmju95.tfm) = %{tl_version}, tex(uwmju96.tfm) = %{tl_version}
Provides:       tex(uwmju97.tfm) = %{tl_version}, tex(uwmju98.tfm) = %{tl_version}
Provides:       tex(uwmju99.tfm) = %{tl_version}, tex(uwmju9a.tfm) = %{tl_version}
Provides:       tex(uwmju9b.tfm) = %{tl_version}, tex(uwmju9c.tfm) = %{tl_version}
Provides:       tex(uwmju9d.tfm) = %{tl_version}, tex(uwmju9e.tfm) = %{tl_version}
Provides:       tex(uwmju9f.tfm) = %{tl_version}, tex(uwmjuac.tfm) = %{tl_version}
Provides:       tex(uwmjuad.tfm) = %{tl_version}, tex(uwmjuae.tfm) = %{tl_version}
Provides:       tex(uwmjuaf.tfm) = %{tl_version}, tex(uwmjub0.tfm) = %{tl_version}
Provides:       tex(uwmjub1.tfm) = %{tl_version}, tex(uwmjub2.tfm) = %{tl_version}
Provides:       tex(uwmjub3.tfm) = %{tl_version}, tex(uwmjub4.tfm) = %{tl_version}
Provides:       tex(uwmjub5.tfm) = %{tl_version}, tex(uwmjub6.tfm) = %{tl_version}
Provides:       tex(uwmjub7.tfm) = %{tl_version}, tex(uwmjub8.tfm) = %{tl_version}
Provides:       tex(uwmjub9.tfm) = %{tl_version}, tex(uwmjuba.tfm) = %{tl_version}
Provides:       tex(uwmjubb.tfm) = %{tl_version}, tex(uwmjubc.tfm) = %{tl_version}
Provides:       tex(uwmjubd.tfm) = %{tl_version}, tex(uwmjube.tfm) = %{tl_version}
Provides:       tex(uwmjubf.tfm) = %{tl_version}, tex(uwmjuc0.tfm) = %{tl_version}
Provides:       tex(uwmjuc1.tfm) = %{tl_version}, tex(uwmjuc2.tfm) = %{tl_version}
Provides:       tex(uwmjuc3.tfm) = %{tl_version}, tex(uwmjuc4.tfm) = %{tl_version}
Provides:       tex(uwmjuc5.tfm) = %{tl_version}, tex(uwmjuc6.tfm) = %{tl_version}
Provides:       tex(uwmjuc7.tfm) = %{tl_version}, tex(uwmjuc8.tfm) = %{tl_version}
Provides:       tex(uwmjuc9.tfm) = %{tl_version}, tex(uwmjuca.tfm) = %{tl_version}
Provides:       tex(uwmjucb.tfm) = %{tl_version}, tex(uwmjucc.tfm) = %{tl_version}
Provides:       tex(uwmjucd.tfm) = %{tl_version}, tex(uwmjuce.tfm) = %{tl_version}
Provides:       tex(uwmjucf.tfm) = %{tl_version}, tex(uwmjud0.tfm) = %{tl_version}
Provides:       tex(uwmjud1.tfm) = %{tl_version}, tex(uwmjud2.tfm) = %{tl_version}
Provides:       tex(uwmjud3.tfm) = %{tl_version}, tex(uwmjud4.tfm) = %{tl_version}
Provides:       tex(uwmjud5.tfm) = %{tl_version}, tex(uwmjud6.tfm) = %{tl_version}
Provides:       tex(uwmjud7.tfm) = %{tl_version}, tex(uwmjuf9.tfm) = %{tl_version}
Provides:       tex(uwmjufa.tfm) = %{tl_version}, tex(uwmjuff.tfm) = %{tl_version}
Provides:       tex(uwmjuo00.tfm) = %{tl_version}, tex(uwmjuo01.tfm) = %{tl_version}
Provides:       tex(uwmjuo02.tfm) = %{tl_version}, tex(uwmjuo03.tfm) = %{tl_version}
Provides:       tex(uwmjuo04.tfm) = %{tl_version}, tex(uwmjuo20.tfm) = %{tl_version}
Provides:       tex(uwmjuo21.tfm) = %{tl_version}, tex(uwmjuo22.tfm) = %{tl_version}
Provides:       tex(uwmjuo23.tfm) = %{tl_version}, tex(uwmjuo24.tfm) = %{tl_version}
Provides:       tex(uwmjuo25.tfm) = %{tl_version}, tex(uwmjuo26.tfm) = %{tl_version}
Provides:       tex(uwmjuo30.tfm) = %{tl_version}, tex(uwmjuo31.tfm) = %{tl_version}
Provides:       tex(uwmjuo32.tfm) = %{tl_version}, tex(uwmjuo33.tfm) = %{tl_version}
Provides:       tex(uwmjuo4e.tfm) = %{tl_version}, tex(uwmjuo4f.tfm) = %{tl_version}
Provides:       tex(uwmjuo50.tfm) = %{tl_version}, tex(uwmjuo51.tfm) = %{tl_version}
Provides:       tex(uwmjuo52.tfm) = %{tl_version}, tex(uwmjuo53.tfm) = %{tl_version}
Provides:       tex(uwmjuo54.tfm) = %{tl_version}, tex(uwmjuo55.tfm) = %{tl_version}
Provides:       tex(uwmjuo56.tfm) = %{tl_version}, tex(uwmjuo57.tfm) = %{tl_version}
Provides:       tex(uwmjuo58.tfm) = %{tl_version}, tex(uwmjuo59.tfm) = %{tl_version}
Provides:       tex(uwmjuo5a.tfm) = %{tl_version}, tex(uwmjuo5b.tfm) = %{tl_version}
Provides:       tex(uwmjuo5c.tfm) = %{tl_version}, tex(uwmjuo5d.tfm) = %{tl_version}
Provides:       tex(uwmjuo5e.tfm) = %{tl_version}, tex(uwmjuo5f.tfm) = %{tl_version}
Provides:       tex(uwmjuo60.tfm) = %{tl_version}, tex(uwmjuo61.tfm) = %{tl_version}
Provides:       tex(uwmjuo62.tfm) = %{tl_version}, tex(uwmjuo63.tfm) = %{tl_version}
Provides:       tex(uwmjuo64.tfm) = %{tl_version}, tex(uwmjuo65.tfm) = %{tl_version}
Provides:       tex(uwmjuo66.tfm) = %{tl_version}, tex(uwmjuo67.tfm) = %{tl_version}
Provides:       tex(uwmjuo68.tfm) = %{tl_version}, tex(uwmjuo69.tfm) = %{tl_version}
Provides:       tex(uwmjuo6a.tfm) = %{tl_version}, tex(uwmjuo6b.tfm) = %{tl_version}
Provides:       tex(uwmjuo6c.tfm) = %{tl_version}, tex(uwmjuo6d.tfm) = %{tl_version}
Provides:       tex(uwmjuo6e.tfm) = %{tl_version}, tex(uwmjuo6f.tfm) = %{tl_version}
Provides:       tex(uwmjuo70.tfm) = %{tl_version}, tex(uwmjuo71.tfm) = %{tl_version}
Provides:       tex(uwmjuo72.tfm) = %{tl_version}, tex(uwmjuo73.tfm) = %{tl_version}
Provides:       tex(uwmjuo74.tfm) = %{tl_version}, tex(uwmjuo75.tfm) = %{tl_version}
Provides:       tex(uwmjuo76.tfm) = %{tl_version}, tex(uwmjuo77.tfm) = %{tl_version}
Provides:       tex(uwmjuo78.tfm) = %{tl_version}, tex(uwmjuo79.tfm) = %{tl_version}
Provides:       tex(uwmjuo7a.tfm) = %{tl_version}, tex(uwmjuo7b.tfm) = %{tl_version}
Provides:       tex(uwmjuo7c.tfm) = %{tl_version}, tex(uwmjuo7d.tfm) = %{tl_version}
Provides:       tex(uwmjuo7e.tfm) = %{tl_version}, tex(uwmjuo7f.tfm) = %{tl_version}
Provides:       tex(uwmjuo80.tfm) = %{tl_version}, tex(uwmjuo81.tfm) = %{tl_version}
Provides:       tex(uwmjuo82.tfm) = %{tl_version}, tex(uwmjuo83.tfm) = %{tl_version}
Provides:       tex(uwmjuo84.tfm) = %{tl_version}, tex(uwmjuo85.tfm) = %{tl_version}
Provides:       tex(uwmjuo86.tfm) = %{tl_version}, tex(uwmjuo87.tfm) = %{tl_version}
Provides:       tex(uwmjuo88.tfm) = %{tl_version}, tex(uwmjuo89.tfm) = %{tl_version}
Provides:       tex(uwmjuo8a.tfm) = %{tl_version}, tex(uwmjuo8b.tfm) = %{tl_version}
Provides:       tex(uwmjuo8c.tfm) = %{tl_version}, tex(uwmjuo8d.tfm) = %{tl_version}
Provides:       tex(uwmjuo8e.tfm) = %{tl_version}, tex(uwmjuo8f.tfm) = %{tl_version}
Provides:       tex(uwmjuo90.tfm) = %{tl_version}, tex(uwmjuo91.tfm) = %{tl_version}
Provides:       tex(uwmjuo92.tfm) = %{tl_version}, tex(uwmjuo93.tfm) = %{tl_version}
Provides:       tex(uwmjuo94.tfm) = %{tl_version}, tex(uwmjuo95.tfm) = %{tl_version}
Provides:       tex(uwmjuo96.tfm) = %{tl_version}, tex(uwmjuo97.tfm) = %{tl_version}
Provides:       tex(uwmjuo98.tfm) = %{tl_version}, tex(uwmjuo99.tfm) = %{tl_version}
Provides:       tex(uwmjuo9a.tfm) = %{tl_version}, tex(uwmjuo9b.tfm) = %{tl_version}
Provides:       tex(uwmjuo9c.tfm) = %{tl_version}, tex(uwmjuo9d.tfm) = %{tl_version}
Provides:       tex(uwmjuo9e.tfm) = %{tl_version}, tex(uwmjuo9f.tfm) = %{tl_version}
Provides:       tex(uwmjuoac.tfm) = %{tl_version}, tex(uwmjuoad.tfm) = %{tl_version}
Provides:       tex(uwmjuoae.tfm) = %{tl_version}, tex(uwmjuoaf.tfm) = %{tl_version}
Provides:       tex(uwmjuob0.tfm) = %{tl_version}, tex(uwmjuob1.tfm) = %{tl_version}
Provides:       tex(uwmjuob2.tfm) = %{tl_version}, tex(uwmjuob3.tfm) = %{tl_version}
Provides:       tex(uwmjuob4.tfm) = %{tl_version}, tex(uwmjuob5.tfm) = %{tl_version}
Provides:       tex(uwmjuob6.tfm) = %{tl_version}, tex(uwmjuob7.tfm) = %{tl_version}
Provides:       tex(uwmjuob8.tfm) = %{tl_version}, tex(uwmjuob9.tfm) = %{tl_version}
Provides:       tex(uwmjuoba.tfm) = %{tl_version}, tex(uwmjuobb.tfm) = %{tl_version}
Provides:       tex(uwmjuobc.tfm) = %{tl_version}, tex(uwmjuobd.tfm) = %{tl_version}
Provides:       tex(uwmjuobe.tfm) = %{tl_version}, tex(uwmjuobf.tfm) = %{tl_version}
Provides:       tex(uwmjuoc0.tfm) = %{tl_version}, tex(uwmjuoc1.tfm) = %{tl_version}
Provides:       tex(uwmjuoc2.tfm) = %{tl_version}, tex(uwmjuoc3.tfm) = %{tl_version}
Provides:       tex(uwmjuoc4.tfm) = %{tl_version}, tex(uwmjuoc5.tfm) = %{tl_version}
Provides:       tex(uwmjuoc6.tfm) = %{tl_version}, tex(uwmjuoc7.tfm) = %{tl_version}
Provides:       tex(uwmjuoc8.tfm) = %{tl_version}, tex(uwmjuoc9.tfm) = %{tl_version}
Provides:       tex(uwmjuoca.tfm) = %{tl_version}, tex(uwmjuocb.tfm) = %{tl_version}
Provides:       tex(uwmjuocc.tfm) = %{tl_version}, tex(uwmjuocd.tfm) = %{tl_version}
Provides:       tex(uwmjuoce.tfm) = %{tl_version}, tex(uwmjuocf.tfm) = %{tl_version}
Provides:       tex(uwmjuod0.tfm) = %{tl_version}, tex(uwmjuod1.tfm) = %{tl_version}
Provides:       tex(uwmjuod2.tfm) = %{tl_version}, tex(uwmjuod3.tfm) = %{tl_version}
Provides:       tex(uwmjuod4.tfm) = %{tl_version}, tex(uwmjuod5.tfm) = %{tl_version}
Provides:       tex(uwmjuod6.tfm) = %{tl_version}, tex(uwmjuod7.tfm) = %{tl_version}
Provides:       tex(uwmjuof9.tfm) = %{tl_version}, tex(uwmjuofa.tfm) = %{tl_version}
Provides:       tex(uwmjuoff.tfm) = %{tl_version}, tex(uwmjx00.tfm) = %{tl_version}
Provides:       tex(uwmjx01.tfm) = %{tl_version}, tex(uwmjx02.tfm) = %{tl_version}
Provides:       tex(uwmjx03.tfm) = %{tl_version}, tex(uwmjx04.tfm) = %{tl_version}
Provides:       tex(uwmjx20.tfm) = %{tl_version}, tex(uwmjx21.tfm) = %{tl_version}
Provides:       tex(uwmjx22.tfm) = %{tl_version}, tex(uwmjx23.tfm) = %{tl_version}
Provides:       tex(uwmjx24.tfm) = %{tl_version}, tex(uwmjx25.tfm) = %{tl_version}
Provides:       tex(uwmjx26.tfm) = %{tl_version}, tex(uwmjx30.tfm) = %{tl_version}
Provides:       tex(uwmjx31.tfm) = %{tl_version}, tex(uwmjx32.tfm) = %{tl_version}
Provides:       tex(uwmjx33.tfm) = %{tl_version}, tex(uwmjx4e.tfm) = %{tl_version}
Provides:       tex(uwmjx4f.tfm) = %{tl_version}, tex(uwmjx50.tfm) = %{tl_version}
Provides:       tex(uwmjx51.tfm) = %{tl_version}, tex(uwmjx52.tfm) = %{tl_version}
Provides:       tex(uwmjx53.tfm) = %{tl_version}, tex(uwmjx54.tfm) = %{tl_version}
Provides:       tex(uwmjx55.tfm) = %{tl_version}, tex(uwmjx56.tfm) = %{tl_version}
Provides:       tex(uwmjx57.tfm) = %{tl_version}, tex(uwmjx58.tfm) = %{tl_version}
Provides:       tex(uwmjx59.tfm) = %{tl_version}, tex(uwmjx5a.tfm) = %{tl_version}
Provides:       tex(uwmjx5b.tfm) = %{tl_version}, tex(uwmjx5c.tfm) = %{tl_version}
Provides:       tex(uwmjx5d.tfm) = %{tl_version}, tex(uwmjx5e.tfm) = %{tl_version}
Provides:       tex(uwmjx5f.tfm) = %{tl_version}, tex(uwmjx60.tfm) = %{tl_version}
Provides:       tex(uwmjx61.tfm) = %{tl_version}, tex(uwmjx62.tfm) = %{tl_version}
Provides:       tex(uwmjx63.tfm) = %{tl_version}, tex(uwmjx64.tfm) = %{tl_version}
Provides:       tex(uwmjx65.tfm) = %{tl_version}, tex(uwmjx66.tfm) = %{tl_version}
Provides:       tex(uwmjx67.tfm) = %{tl_version}, tex(uwmjx68.tfm) = %{tl_version}
Provides:       tex(uwmjx69.tfm) = %{tl_version}, tex(uwmjx6a.tfm) = %{tl_version}
Provides:       tex(uwmjx6b.tfm) = %{tl_version}, tex(uwmjx6c.tfm) = %{tl_version}
Provides:       tex(uwmjx6d.tfm) = %{tl_version}, tex(uwmjx6e.tfm) = %{tl_version}
Provides:       tex(uwmjx6f.tfm) = %{tl_version}, tex(uwmjx70.tfm) = %{tl_version}
Provides:       tex(uwmjx71.tfm) = %{tl_version}, tex(uwmjx72.tfm) = %{tl_version}
Provides:       tex(uwmjx73.tfm) = %{tl_version}, tex(uwmjx74.tfm) = %{tl_version}
Provides:       tex(uwmjx75.tfm) = %{tl_version}, tex(uwmjx76.tfm) = %{tl_version}
Provides:       tex(uwmjx77.tfm) = %{tl_version}, tex(uwmjx78.tfm) = %{tl_version}
Provides:       tex(uwmjx79.tfm) = %{tl_version}, tex(uwmjx7a.tfm) = %{tl_version}
Provides:       tex(uwmjx7b.tfm) = %{tl_version}, tex(uwmjx7c.tfm) = %{tl_version}
Provides:       tex(uwmjx7d.tfm) = %{tl_version}, tex(uwmjx7e.tfm) = %{tl_version}
Provides:       tex(uwmjx7f.tfm) = %{tl_version}, tex(uwmjx80.tfm) = %{tl_version}
Provides:       tex(uwmjx81.tfm) = %{tl_version}, tex(uwmjx82.tfm) = %{tl_version}
Provides:       tex(uwmjx83.tfm) = %{tl_version}, tex(uwmjx84.tfm) = %{tl_version}
Provides:       tex(uwmjx85.tfm) = %{tl_version}, tex(uwmjx86.tfm) = %{tl_version}
Provides:       tex(uwmjx87.tfm) = %{tl_version}, tex(uwmjx88.tfm) = %{tl_version}
Provides:       tex(uwmjx89.tfm) = %{tl_version}, tex(uwmjx8a.tfm) = %{tl_version}
Provides:       tex(uwmjx8b.tfm) = %{tl_version}, tex(uwmjx8c.tfm) = %{tl_version}
Provides:       tex(uwmjx8d.tfm) = %{tl_version}, tex(uwmjx8e.tfm) = %{tl_version}
Provides:       tex(uwmjx8f.tfm) = %{tl_version}, tex(uwmjx90.tfm) = %{tl_version}
Provides:       tex(uwmjx91.tfm) = %{tl_version}, tex(uwmjx92.tfm) = %{tl_version}
Provides:       tex(uwmjx93.tfm) = %{tl_version}, tex(uwmjx94.tfm) = %{tl_version}
Provides:       tex(uwmjx95.tfm) = %{tl_version}, tex(uwmjx96.tfm) = %{tl_version}
Provides:       tex(uwmjx97.tfm) = %{tl_version}, tex(uwmjx98.tfm) = %{tl_version}
Provides:       tex(uwmjx99.tfm) = %{tl_version}, tex(uwmjx9a.tfm) = %{tl_version}
Provides:       tex(uwmjx9b.tfm) = %{tl_version}, tex(uwmjx9c.tfm) = %{tl_version}
Provides:       tex(uwmjx9d.tfm) = %{tl_version}, tex(uwmjx9e.tfm) = %{tl_version}
Provides:       tex(uwmjx9f.tfm) = %{tl_version}, tex(uwmjxac.tfm) = %{tl_version}
Provides:       tex(uwmjxad.tfm) = %{tl_version}, tex(uwmjxae.tfm) = %{tl_version}
Provides:       tex(uwmjxaf.tfm) = %{tl_version}, tex(uwmjxb0.tfm) = %{tl_version}
Provides:       tex(uwmjxb1.tfm) = %{tl_version}, tex(uwmjxb2.tfm) = %{tl_version}
Provides:       tex(uwmjxb3.tfm) = %{tl_version}, tex(uwmjxb4.tfm) = %{tl_version}
Provides:       tex(uwmjxb5.tfm) = %{tl_version}, tex(uwmjxb6.tfm) = %{tl_version}
Provides:       tex(uwmjxb7.tfm) = %{tl_version}, tex(uwmjxb8.tfm) = %{tl_version}
Provides:       tex(uwmjxb9.tfm) = %{tl_version}, tex(uwmjxba.tfm) = %{tl_version}
Provides:       tex(uwmjxbb.tfm) = %{tl_version}, tex(uwmjxbc.tfm) = %{tl_version}
Provides:       tex(uwmjxbd.tfm) = %{tl_version}, tex(uwmjxbe.tfm) = %{tl_version}
Provides:       tex(uwmjxbf.tfm) = %{tl_version}, tex(uwmjxc0.tfm) = %{tl_version}
Provides:       tex(uwmjxc1.tfm) = %{tl_version}, tex(uwmjxc2.tfm) = %{tl_version}
Provides:       tex(uwmjxc3.tfm) = %{tl_version}, tex(uwmjxc4.tfm) = %{tl_version}
Provides:       tex(uwmjxc5.tfm) = %{tl_version}, tex(uwmjxc6.tfm) = %{tl_version}
Provides:       tex(uwmjxc7.tfm) = %{tl_version}, tex(uwmjxc8.tfm) = %{tl_version}
Provides:       tex(uwmjxc9.tfm) = %{tl_version}, tex(uwmjxca.tfm) = %{tl_version}
Provides:       tex(uwmjxcb.tfm) = %{tl_version}, tex(uwmjxcc.tfm) = %{tl_version}
Provides:       tex(uwmjxcd.tfm) = %{tl_version}, tex(uwmjxce.tfm) = %{tl_version}
Provides:       tex(uwmjxcf.tfm) = %{tl_version}, tex(uwmjxd0.tfm) = %{tl_version}
Provides:       tex(uwmjxd1.tfm) = %{tl_version}, tex(uwmjxd2.tfm) = %{tl_version}
Provides:       tex(uwmjxd3.tfm) = %{tl_version}, tex(uwmjxd4.tfm) = %{tl_version}
Provides:       tex(uwmjxd5.tfm) = %{tl_version}, tex(uwmjxd6.tfm) = %{tl_version}
Provides:       tex(uwmjxd7.tfm) = %{tl_version}, tex(uwmjxf9.tfm) = %{tl_version}
Provides:       tex(uwmjxfa.tfm) = %{tl_version}, tex(uwmjxff.tfm) = %{tl_version}
Provides:       tex(uwmjxo00.tfm) = %{tl_version}, tex(uwmjxo01.tfm) = %{tl_version}
Provides:       tex(uwmjxo02.tfm) = %{tl_version}, tex(uwmjxo03.tfm) = %{tl_version}
Provides:       tex(uwmjxo04.tfm) = %{tl_version}, tex(uwmjxo20.tfm) = %{tl_version}
Provides:       tex(uwmjxo21.tfm) = %{tl_version}, tex(uwmjxo22.tfm) = %{tl_version}
Provides:       tex(uwmjxo23.tfm) = %{tl_version}, tex(uwmjxo24.tfm) = %{tl_version}
Provides:       tex(uwmjxo25.tfm) = %{tl_version}, tex(uwmjxo26.tfm) = %{tl_version}
Provides:       tex(uwmjxo30.tfm) = %{tl_version}, tex(uwmjxo31.tfm) = %{tl_version}
Provides:       tex(uwmjxo32.tfm) = %{tl_version}, tex(uwmjxo33.tfm) = %{tl_version}
Provides:       tex(uwmjxo4e.tfm) = %{tl_version}, tex(uwmjxo4f.tfm) = %{tl_version}
Provides:       tex(uwmjxo50.tfm) = %{tl_version}, tex(uwmjxo51.tfm) = %{tl_version}
Provides:       tex(uwmjxo52.tfm) = %{tl_version}, tex(uwmjxo53.tfm) = %{tl_version}
Provides:       tex(uwmjxo54.tfm) = %{tl_version}, tex(uwmjxo55.tfm) = %{tl_version}
Provides:       tex(uwmjxo56.tfm) = %{tl_version}, tex(uwmjxo57.tfm) = %{tl_version}
Provides:       tex(uwmjxo58.tfm) = %{tl_version}, tex(uwmjxo59.tfm) = %{tl_version}
Provides:       tex(uwmjxo5a.tfm) = %{tl_version}, tex(uwmjxo5b.tfm) = %{tl_version}
Provides:       tex(uwmjxo5c.tfm) = %{tl_version}, tex(uwmjxo5d.tfm) = %{tl_version}
Provides:       tex(uwmjxo5e.tfm) = %{tl_version}, tex(uwmjxo5f.tfm) = %{tl_version}
Provides:       tex(uwmjxo60.tfm) = %{tl_version}, tex(uwmjxo61.tfm) = %{tl_version}
Provides:       tex(uwmjxo62.tfm) = %{tl_version}, tex(uwmjxo63.tfm) = %{tl_version}
Provides:       tex(uwmjxo64.tfm) = %{tl_version}, tex(uwmjxo65.tfm) = %{tl_version}
Provides:       tex(uwmjxo66.tfm) = %{tl_version}, tex(uwmjxo67.tfm) = %{tl_version}
Provides:       tex(uwmjxo68.tfm) = %{tl_version}, tex(uwmjxo69.tfm) = %{tl_version}
Provides:       tex(uwmjxo6a.tfm) = %{tl_version}, tex(uwmjxo6b.tfm) = %{tl_version}
Provides:       tex(uwmjxo6c.tfm) = %{tl_version}, tex(uwmjxo6d.tfm) = %{tl_version}
Provides:       tex(uwmjxo6e.tfm) = %{tl_version}, tex(uwmjxo6f.tfm) = %{tl_version}
Provides:       tex(uwmjxo70.tfm) = %{tl_version}, tex(uwmjxo71.tfm) = %{tl_version}
Provides:       tex(uwmjxo72.tfm) = %{tl_version}, tex(uwmjxo73.tfm) = %{tl_version}
Provides:       tex(uwmjxo74.tfm) = %{tl_version}, tex(uwmjxo75.tfm) = %{tl_version}
Provides:       tex(uwmjxo76.tfm) = %{tl_version}, tex(uwmjxo77.tfm) = %{tl_version}
Provides:       tex(uwmjxo78.tfm) = %{tl_version}, tex(uwmjxo79.tfm) = %{tl_version}
Provides:       tex(uwmjxo7a.tfm) = %{tl_version}, tex(uwmjxo7b.tfm) = %{tl_version}
Provides:       tex(uwmjxo7c.tfm) = %{tl_version}, tex(uwmjxo7d.tfm) = %{tl_version}
Provides:       tex(uwmjxo7e.tfm) = %{tl_version}, tex(uwmjxo7f.tfm) = %{tl_version}
Provides:       tex(uwmjxo80.tfm) = %{tl_version}, tex(uwmjxo81.tfm) = %{tl_version}
Provides:       tex(uwmjxo82.tfm) = %{tl_version}, tex(uwmjxo83.tfm) = %{tl_version}
Provides:       tex(uwmjxo84.tfm) = %{tl_version}, tex(uwmjxo85.tfm) = %{tl_version}
Provides:       tex(uwmjxo86.tfm) = %{tl_version}, tex(uwmjxo87.tfm) = %{tl_version}
Provides:       tex(uwmjxo88.tfm) = %{tl_version}, tex(uwmjxo89.tfm) = %{tl_version}
Provides:       tex(uwmjxo8a.tfm) = %{tl_version}, tex(uwmjxo8b.tfm) = %{tl_version}
Provides:       tex(uwmjxo8c.tfm) = %{tl_version}, tex(uwmjxo8d.tfm) = %{tl_version}
Provides:       tex(uwmjxo8e.tfm) = %{tl_version}, tex(uwmjxo8f.tfm) = %{tl_version}
Provides:       tex(uwmjxo90.tfm) = %{tl_version}, tex(uwmjxo91.tfm) = %{tl_version}
Provides:       tex(uwmjxo92.tfm) = %{tl_version}, tex(uwmjxo93.tfm) = %{tl_version}
Provides:       tex(uwmjxo94.tfm) = %{tl_version}, tex(uwmjxo95.tfm) = %{tl_version}
Provides:       tex(uwmjxo96.tfm) = %{tl_version}, tex(uwmjxo97.tfm) = %{tl_version}
Provides:       tex(uwmjxo98.tfm) = %{tl_version}, tex(uwmjxo99.tfm) = %{tl_version}
Provides:       tex(uwmjxo9a.tfm) = %{tl_version}, tex(uwmjxo9b.tfm) = %{tl_version}
Provides:       tex(uwmjxo9c.tfm) = %{tl_version}, tex(uwmjxo9d.tfm) = %{tl_version}
Provides:       tex(uwmjxo9e.tfm) = %{tl_version}, tex(uwmjxo9f.tfm) = %{tl_version}
Provides:       tex(uwmjxoac.tfm) = %{tl_version}, tex(uwmjxoad.tfm) = %{tl_version}
Provides:       tex(uwmjxoae.tfm) = %{tl_version}, tex(uwmjxoaf.tfm) = %{tl_version}
Provides:       tex(uwmjxob0.tfm) = %{tl_version}, tex(uwmjxob1.tfm) = %{tl_version}
Provides:       tex(uwmjxob2.tfm) = %{tl_version}, tex(uwmjxob3.tfm) = %{tl_version}
Provides:       tex(uwmjxob4.tfm) = %{tl_version}, tex(uwmjxob5.tfm) = %{tl_version}
Provides:       tex(uwmjxob6.tfm) = %{tl_version}, tex(uwmjxob7.tfm) = %{tl_version}
Provides:       tex(uwmjxob8.tfm) = %{tl_version}, tex(uwmjxob9.tfm) = %{tl_version}
Provides:       tex(uwmjxoba.tfm) = %{tl_version}, tex(uwmjxobb.tfm) = %{tl_version}
Provides:       tex(uwmjxobc.tfm) = %{tl_version}, tex(uwmjxobd.tfm) = %{tl_version}
Provides:       tex(uwmjxobe.tfm) = %{tl_version}, tex(uwmjxobf.tfm) = %{tl_version}
Provides:       tex(uwmjxoc0.tfm) = %{tl_version}, tex(uwmjxoc1.tfm) = %{tl_version}
Provides:       tex(uwmjxoc2.tfm) = %{tl_version}, tex(uwmjxoc3.tfm) = %{tl_version}
Provides:       tex(uwmjxoc4.tfm) = %{tl_version}, tex(uwmjxoc5.tfm) = %{tl_version}
Provides:       tex(uwmjxoc6.tfm) = %{tl_version}, tex(uwmjxoc7.tfm) = %{tl_version}
Provides:       tex(uwmjxoc8.tfm) = %{tl_version}, tex(uwmjxoc9.tfm) = %{tl_version}
Provides:       tex(uwmjxoca.tfm) = %{tl_version}, tex(uwmjxocb.tfm) = %{tl_version}
Provides:       tex(uwmjxocc.tfm) = %{tl_version}, tex(uwmjxocd.tfm) = %{tl_version}
Provides:       tex(uwmjxoce.tfm) = %{tl_version}, tex(uwmjxocf.tfm) = %{tl_version}
Provides:       tex(uwmjxod0.tfm) = %{tl_version}, tex(uwmjxod1.tfm) = %{tl_version}
Provides:       tex(uwmjxod2.tfm) = %{tl_version}, tex(uwmjxod3.tfm) = %{tl_version}
Provides:       tex(uwmjxod4.tfm) = %{tl_version}, tex(uwmjxod5.tfm) = %{tl_version}
Provides:       tex(uwmjxod6.tfm) = %{tl_version}, tex(uwmjxod7.tfm) = %{tl_version}
Provides:       tex(uwmjxof9.tfm) = %{tl_version}, tex(uwmjxofa.tfm) = %{tl_version}
Provides:       tex(uwmjxoff.tfm) = %{tl_version}, tex(wmj0.tfm) = %{tl_version}
Provides:       tex(wmj04.tfm) = %{tl_version}, tex(wmj05.tfm) = %{tl_version}
Provides:       tex(wmj06.tfm) = %{tl_version}, tex(wmj07.tfm) = %{tl_version}
Provides:       tex(wmj1.tfm) = %{tl_version}, tex(wmj10.tfm) = %{tl_version}
Provides:       tex(wmj11.tfm) = %{tl_version}, tex(wmj12.tfm) = %{tl_version}
Provides:       tex(wmj13.tfm) = %{tl_version}, tex(wmj14.tfm) = %{tl_version}
Provides:       tex(wmj15.tfm) = %{tl_version}, tex(wmj16.tfm) = %{tl_version}
Provides:       tex(wmj17.tfm) = %{tl_version}, tex(wmj18.tfm) = %{tl_version}
Provides:       tex(wmj19.tfm) = %{tl_version}, tex(wmj2.tfm) = %{tl_version}
Provides:       tex(wmj20.tfm) = %{tl_version}, tex(wmj21.tfm) = %{tl_version}
Provides:       tex(wmj22.tfm) = %{tl_version}, tex(wmj23.tfm) = %{tl_version}
Provides:       tex(wmj24.tfm) = %{tl_version}, tex(wmj25.tfm) = %{tl_version}
Provides:       tex(wmj26.tfm) = %{tl_version}, tex(wmj27.tfm) = %{tl_version}
Provides:       tex(wmj28.tfm) = %{tl_version}, tex(wmj29.tfm) = %{tl_version}
Provides:       tex(wmj3.tfm) = %{tl_version}, tex(wmj4.tfm) = %{tl_version}
Provides:       tex(wmj5.tfm) = %{tl_version}, tex(wmj6.tfm) = %{tl_version}
Provides:       tex(wmj7.tfm) = %{tl_version}, tex(wmj8.tfm) = %{tl_version}
Provides:       tex(wmj9.tfm) = %{tl_version}, tex(wmjc0.tfm) = %{tl_version}
Provides:       tex(wmjc04.tfm) = %{tl_version}, tex(wmjc05.tfm) = %{tl_version}
Provides:       tex(wmjc06.tfm) = %{tl_version}, tex(wmjc07.tfm) = %{tl_version}
Provides:       tex(wmjc1.tfm) = %{tl_version}, tex(wmjc10.tfm) = %{tl_version}
Provides:       tex(wmjc11.tfm) = %{tl_version}, tex(wmjc12.tfm) = %{tl_version}
Provides:       tex(wmjc13.tfm) = %{tl_version}, tex(wmjc14.tfm) = %{tl_version}
Provides:       tex(wmjc15.tfm) = %{tl_version}, tex(wmjc16.tfm) = %{tl_version}
Provides:       tex(wmjc17.tfm) = %{tl_version}, tex(wmjc18.tfm) = %{tl_version}
Provides:       tex(wmjc19.tfm) = %{tl_version}, tex(wmjc2.tfm) = %{tl_version}
Provides:       tex(wmjc20.tfm) = %{tl_version}, tex(wmjc21.tfm) = %{tl_version}
Provides:       tex(wmjc22.tfm) = %{tl_version}, tex(wmjc23.tfm) = %{tl_version}
Provides:       tex(wmjc24.tfm) = %{tl_version}, tex(wmjc25.tfm) = %{tl_version}
Provides:       tex(wmjc26.tfm) = %{tl_version}, tex(wmjc27.tfm) = %{tl_version}
Provides:       tex(wmjc28.tfm) = %{tl_version}, tex(wmjc29.tfm) = %{tl_version}
Provides:       tex(wmjc3.tfm) = %{tl_version}, tex(wmjc4.tfm) = %{tl_version}
Provides:       tex(wmjc5.tfm) = %{tl_version}, tex(wmjc6.tfm) = %{tl_version}
Provides:       tex(wmjc7.tfm) = %{tl_version}, tex(wmjc8.tfm) = %{tl_version}
Provides:       tex(wmjc9.tfm) = %{tl_version}, tex(wmjco0.tfm) = %{tl_version}
Provides:       tex(wmjco04.tfm) = %{tl_version}, tex(wmjco05.tfm) = %{tl_version}
Provides:       tex(wmjco06.tfm) = %{tl_version}, tex(wmjco07.tfm) = %{tl_version}
Provides:       tex(wmjco1.tfm) = %{tl_version}, tex(wmjco10.tfm) = %{tl_version}
Provides:       tex(wmjco11.tfm) = %{tl_version}, tex(wmjco12.tfm) = %{tl_version}
Provides:       tex(wmjco13.tfm) = %{tl_version}, tex(wmjco14.tfm) = %{tl_version}
Provides:       tex(wmjco15.tfm) = %{tl_version}, tex(wmjco16.tfm) = %{tl_version}
Provides:       tex(wmjco17.tfm) = %{tl_version}, tex(wmjco18.tfm) = %{tl_version}
Provides:       tex(wmjco19.tfm) = %{tl_version}, tex(wmjco2.tfm) = %{tl_version}
Provides:       tex(wmjco20.tfm) = %{tl_version}, tex(wmjco21.tfm) = %{tl_version}
Provides:       tex(wmjco22.tfm) = %{tl_version}, tex(wmjco23.tfm) = %{tl_version}
Provides:       tex(wmjco24.tfm) = %{tl_version}, tex(wmjco25.tfm) = %{tl_version}
Provides:       tex(wmjco26.tfm) = %{tl_version}, tex(wmjco27.tfm) = %{tl_version}
Provides:       tex(wmjco28.tfm) = %{tl_version}, tex(wmjco29.tfm) = %{tl_version}
Provides:       tex(wmjco3.tfm) = %{tl_version}, tex(wmjco4.tfm) = %{tl_version}
Provides:       tex(wmjco5.tfm) = %{tl_version}, tex(wmjco6.tfm) = %{tl_version}
Provides:       tex(wmjco7.tfm) = %{tl_version}, tex(wmjco8.tfm) = %{tl_version}
Provides:       tex(wmjco9.tfm) = %{tl_version}, tex(wmjo0.tfm) = %{tl_version}
Provides:       tex(wmjo04.tfm) = %{tl_version}, tex(wmjo05.tfm) = %{tl_version}
Provides:       tex(wmjo06.tfm) = %{tl_version}, tex(wmjo07.tfm) = %{tl_version}
Provides:       tex(wmjo1.tfm) = %{tl_version}, tex(wmjo10.tfm) = %{tl_version}
Provides:       tex(wmjo11.tfm) = %{tl_version}, tex(wmjo12.tfm) = %{tl_version}
Provides:       tex(wmjo13.tfm) = %{tl_version}, tex(wmjo14.tfm) = %{tl_version}
Provides:       tex(wmjo15.tfm) = %{tl_version}, tex(wmjo16.tfm) = %{tl_version}
Provides:       tex(wmjo17.tfm) = %{tl_version}, tex(wmjo18.tfm) = %{tl_version}
Provides:       tex(wmjo19.tfm) = %{tl_version}, tex(wmjo2.tfm) = %{tl_version}
Provides:       tex(wmjo20.tfm) = %{tl_version}, tex(wmjo21.tfm) = %{tl_version}
Provides:       tex(wmjo22.tfm) = %{tl_version}, tex(wmjo23.tfm) = %{tl_version}
Provides:       tex(wmjo24.tfm) = %{tl_version}, tex(wmjo25.tfm) = %{tl_version}
Provides:       tex(wmjo26.tfm) = %{tl_version}, tex(wmjo27.tfm) = %{tl_version}
Provides:       tex(wmjo28.tfm) = %{tl_version}, tex(wmjo29.tfm) = %{tl_version}
Provides:       tex(wmjo3.tfm) = %{tl_version}, tex(wmjo4.tfm) = %{tl_version}
Provides:       tex(wmjo5.tfm) = %{tl_version}, tex(wmjo6.tfm) = %{tl_version}
Provides:       tex(wmjo7.tfm) = %{tl_version}, tex(wmjo8.tfm) = %{tl_version}
Provides:       tex(wmjo9.tfm) = %{tl_version}, tex(wmju0.tfm) = %{tl_version}
Provides:       tex(wmju04.tfm) = %{tl_version}, tex(wmju05.tfm) = %{tl_version}
Provides:       tex(wmju06.tfm) = %{tl_version}, tex(wmju07.tfm) = %{tl_version}
Provides:       tex(wmju1.tfm) = %{tl_version}, tex(wmju10.tfm) = %{tl_version}
Provides:       tex(wmju11.tfm) = %{tl_version}, tex(wmju12.tfm) = %{tl_version}
Provides:       tex(wmju13.tfm) = %{tl_version}, tex(wmju14.tfm) = %{tl_version}
Provides:       tex(wmju15.tfm) = %{tl_version}, tex(wmju16.tfm) = %{tl_version}
Provides:       tex(wmju17.tfm) = %{tl_version}, tex(wmju18.tfm) = %{tl_version}
Provides:       tex(wmju19.tfm) = %{tl_version}, tex(wmju2.tfm) = %{tl_version}
Provides:       tex(wmju20.tfm) = %{tl_version}, tex(wmju21.tfm) = %{tl_version}
Provides:       tex(wmju22.tfm) = %{tl_version}, tex(wmju23.tfm) = %{tl_version}
Provides:       tex(wmju24.tfm) = %{tl_version}, tex(wmju25.tfm) = %{tl_version}
Provides:       tex(wmju26.tfm) = %{tl_version}, tex(wmju27.tfm) = %{tl_version}
Provides:       tex(wmju28.tfm) = %{tl_version}, tex(wmju29.tfm) = %{tl_version}
Provides:       tex(wmju3.tfm) = %{tl_version}, tex(wmju4.tfm) = %{tl_version}
Provides:       tex(wmju5.tfm) = %{tl_version}, tex(wmju6.tfm) = %{tl_version}
Provides:       tex(wmju7.tfm) = %{tl_version}, tex(wmju8.tfm) = %{tl_version}
Provides:       tex(wmju9.tfm) = %{tl_version}, tex(wmjuo0.tfm) = %{tl_version}
Provides:       tex(wmjuo04.tfm) = %{tl_version}, tex(wmjuo05.tfm) = %{tl_version}
Provides:       tex(wmjuo06.tfm) = %{tl_version}, tex(wmjuo07.tfm) = %{tl_version}
Provides:       tex(wmjuo1.tfm) = %{tl_version}, tex(wmjuo10.tfm) = %{tl_version}
Provides:       tex(wmjuo11.tfm) = %{tl_version}, tex(wmjuo12.tfm) = %{tl_version}
Provides:       tex(wmjuo13.tfm) = %{tl_version}, tex(wmjuo14.tfm) = %{tl_version}
Provides:       tex(wmjuo15.tfm) = %{tl_version}, tex(wmjuo16.tfm) = %{tl_version}
Provides:       tex(wmjuo17.tfm) = %{tl_version}, tex(wmjuo18.tfm) = %{tl_version}
Provides:       tex(wmjuo19.tfm) = %{tl_version}, tex(wmjuo2.tfm) = %{tl_version}
Provides:       tex(wmjuo20.tfm) = %{tl_version}, tex(wmjuo21.tfm) = %{tl_version}
Provides:       tex(wmjuo22.tfm) = %{tl_version}, tex(wmjuo23.tfm) = %{tl_version}
Provides:       tex(wmjuo24.tfm) = %{tl_version}, tex(wmjuo25.tfm) = %{tl_version}
Provides:       tex(wmjuo26.tfm) = %{tl_version}, tex(wmjuo27.tfm) = %{tl_version}
Provides:       tex(wmjuo28.tfm) = %{tl_version}, tex(wmjuo29.tfm) = %{tl_version}
Provides:       tex(wmjuo3.tfm) = %{tl_version}, tex(wmjuo4.tfm) = %{tl_version}
Provides:       tex(wmjuo5.tfm) = %{tl_version}, tex(wmjuo6.tfm) = %{tl_version}
Provides:       tex(wmjuo7.tfm) = %{tl_version}, tex(wmjuo8.tfm) = %{tl_version}
Provides:       tex(wmjuo9.tfm) = %{tl_version}, tex(wmjx0.tfm) = %{tl_version}
Provides:       tex(wmjx04.tfm) = %{tl_version}, tex(wmjx05.tfm) = %{tl_version}
Provides:       tex(wmjx06.tfm) = %{tl_version}, tex(wmjx07.tfm) = %{tl_version}
Provides:       tex(wmjx1.tfm) = %{tl_version}, tex(wmjx10.tfm) = %{tl_version}
Provides:       tex(wmjx11.tfm) = %{tl_version}, tex(wmjx12.tfm) = %{tl_version}
Provides:       tex(wmjx13.tfm) = %{tl_version}, tex(wmjx14.tfm) = %{tl_version}
Provides:       tex(wmjx15.tfm) = %{tl_version}, tex(wmjx16.tfm) = %{tl_version}
Provides:       tex(wmjx17.tfm) = %{tl_version}, tex(wmjx18.tfm) = %{tl_version}
Provides:       tex(wmjx19.tfm) = %{tl_version}, tex(wmjx2.tfm) = %{tl_version}
Provides:       tex(wmjx20.tfm) = %{tl_version}, tex(wmjx21.tfm) = %{tl_version}
Provides:       tex(wmjx22.tfm) = %{tl_version}, tex(wmjx23.tfm) = %{tl_version}
Provides:       tex(wmjx24.tfm) = %{tl_version}, tex(wmjx25.tfm) = %{tl_version}
Provides:       tex(wmjx26.tfm) = %{tl_version}, tex(wmjx27.tfm) = %{tl_version}
Provides:       tex(wmjx28.tfm) = %{tl_version}, tex(wmjx29.tfm) = %{tl_version}
Provides:       tex(wmjx3.tfm) = %{tl_version}, tex(wmjx4.tfm) = %{tl_version}
Provides:       tex(wmjx5.tfm) = %{tl_version}, tex(wmjx6.tfm) = %{tl_version}
Provides:       tex(wmjx7.tfm) = %{tl_version}, tex(wmjx8.tfm) = %{tl_version}
Provides:       tex(wmjx9.tfm) = %{tl_version}, tex(wmjxo0.tfm) = %{tl_version}
Provides:       tex(wmjxo04.tfm) = %{tl_version}, tex(wmjxo05.tfm) = %{tl_version}
Provides:       tex(wmjxo06.tfm) = %{tl_version}, tex(wmjxo07.tfm) = %{tl_version}
Provides:       tex(wmjxo1.tfm) = %{tl_version}, tex(wmjxo10.tfm) = %{tl_version}
Provides:       tex(wmjxo11.tfm) = %{tl_version}, tex(wmjxo12.tfm) = %{tl_version}
Provides:       tex(wmjxo13.tfm) = %{tl_version}, tex(wmjxo14.tfm) = %{tl_version}
Provides:       tex(wmjxo15.tfm) = %{tl_version}, tex(wmjxo16.tfm) = %{tl_version}
Provides:       tex(wmjxo17.tfm) = %{tl_version}, tex(wmjxo18.tfm) = %{tl_version}
Provides:       tex(wmjxo19.tfm) = %{tl_version}, tex(wmjxo2.tfm) = %{tl_version}
Provides:       tex(wmjxo20.tfm) = %{tl_version}, tex(wmjxo21.tfm) = %{tl_version}
Provides:       tex(wmjxo22.tfm) = %{tl_version}, tex(wmjxo23.tfm) = %{tl_version}
Provides:       tex(wmjxo24.tfm) = %{tl_version}, tex(wmjxo25.tfm) = %{tl_version}
Provides:       tex(wmjxo26.tfm) = %{tl_version}, tex(wmjxo27.tfm) = %{tl_version}
Provides:       tex(wmjxo28.tfm) = %{tl_version}, tex(wmjxo29.tfm) = %{tl_version}
Provides:       tex(wmjxo3.tfm) = %{tl_version}, tex(wmjxo4.tfm) = %{tl_version}
Provides:       tex(wmjxo5.tfm) = %{tl_version}, tex(wmjxo6.tfm) = %{tl_version}
Provides:       tex(wmjxo7.tfm) = %{tl_version}, tex(wmjxo8.tfm) = %{tl_version}
Provides:       tex(wmjxo9.tfm) = %{tl_version}, tex(umj00.pfb) = %{tl_version}
Provides:       tex(umj01.pfb) = %{tl_version}, tex(umj02.pfb) = %{tl_version}
Provides:       tex(umj03.pfb) = %{tl_version}, tex(umj04.pfb) = %{tl_version}
Provides:       tex(umj05.pfb) = %{tl_version}, tex(umj10.pfb) = %{tl_version}
Provides:       tex(umj11.pfb) = %{tl_version}, tex(umj12.pfb) = %{tl_version}
Provides:       tex(umj13.pfb) = %{tl_version}, tex(umj14.pfb) = %{tl_version}
Provides:       tex(umj15.pfb) = %{tl_version}, tex(umj16.pfb) = %{tl_version}
Provides:       tex(umj17.pfb) = %{tl_version}, tex(umj20.pfb) = %{tl_version}
Provides:       tex(umj21.pfb) = %{tl_version}, tex(umj22.pfb) = %{tl_version}
Provides:       tex(umj23.pfb) = %{tl_version}, tex(umj24.pfb) = %{tl_version}
Provides:       tex(umj25.pfb) = %{tl_version}, tex(umj26.pfb) = %{tl_version}
Provides:       tex(umj27.pfb) = %{tl_version}, tex(umj28.pfb) = %{tl_version}
Provides:       tex(umj29.pfb) = %{tl_version}, tex(umj30.pfb) = %{tl_version}
Provides:       tex(umj31.pfb) = %{tl_version}, tex(umj32.pfb) = %{tl_version}
Provides:       tex(umj33.pfb) = %{tl_version}, tex(umj34.pfb) = %{tl_version}
Provides:       tex(umj35.pfb) = %{tl_version}, tex(umj36.pfb) = %{tl_version}
Provides:       tex(umj37.pfb) = %{tl_version}, tex(umj38.pfb) = %{tl_version}
Provides:       tex(uwmj00.vf) = %{tl_version}, tex(uwmj01.vf) = %{tl_version}
Provides:       tex(uwmj02.vf) = %{tl_version}, tex(uwmj03.vf) = %{tl_version}
Provides:       tex(uwmj04.vf) = %{tl_version}, tex(uwmj20.vf) = %{tl_version}
Provides:       tex(uwmj21.vf) = %{tl_version}, tex(uwmj22.vf) = %{tl_version}
Provides:       tex(uwmj23.vf) = %{tl_version}, tex(uwmj24.vf) = %{tl_version}
Provides:       tex(uwmj25.vf) = %{tl_version}, tex(uwmj26.vf) = %{tl_version}
Provides:       tex(uwmj30.vf) = %{tl_version}, tex(uwmj31.vf) = %{tl_version}
Provides:       tex(uwmj32.vf) = %{tl_version}, tex(uwmj33.vf) = %{tl_version}
Provides:       tex(uwmj4e.vf) = %{tl_version}, tex(uwmj4f.vf) = %{tl_version}
Provides:       tex(uwmj50.vf) = %{tl_version}, tex(uwmj51.vf) = %{tl_version}
Provides:       tex(uwmj52.vf) = %{tl_version}, tex(uwmj53.vf) = %{tl_version}
Provides:       tex(uwmj54.vf) = %{tl_version}, tex(uwmj55.vf) = %{tl_version}
Provides:       tex(uwmj56.vf) = %{tl_version}, tex(uwmj57.vf) = %{tl_version}
Provides:       tex(uwmj58.vf) = %{tl_version}, tex(uwmj59.vf) = %{tl_version}
Provides:       tex(uwmj5a.vf) = %{tl_version}, tex(uwmj5b.vf) = %{tl_version}
Provides:       tex(uwmj5c.vf) = %{tl_version}, tex(uwmj5d.vf) = %{tl_version}
Provides:       tex(uwmj5e.vf) = %{tl_version}, tex(uwmj5f.vf) = %{tl_version}
Provides:       tex(uwmj60.vf) = %{tl_version}, tex(uwmj61.vf) = %{tl_version}
Provides:       tex(uwmj62.vf) = %{tl_version}, tex(uwmj63.vf) = %{tl_version}
Provides:       tex(uwmj64.vf) = %{tl_version}, tex(uwmj65.vf) = %{tl_version}
Provides:       tex(uwmj66.vf) = %{tl_version}, tex(uwmj67.vf) = %{tl_version}
Provides:       tex(uwmj68.vf) = %{tl_version}, tex(uwmj69.vf) = %{tl_version}
Provides:       tex(uwmj6a.vf) = %{tl_version}, tex(uwmj6b.vf) = %{tl_version}
Provides:       tex(uwmj6c.vf) = %{tl_version}, tex(uwmj6d.vf) = %{tl_version}
Provides:       tex(uwmj6e.vf) = %{tl_version}, tex(uwmj6f.vf) = %{tl_version}
Provides:       tex(uwmj70.vf) = %{tl_version}, tex(uwmj71.vf) = %{tl_version}
Provides:       tex(uwmj72.vf) = %{tl_version}, tex(uwmj73.vf) = %{tl_version}
Provides:       tex(uwmj74.vf) = %{tl_version}, tex(uwmj75.vf) = %{tl_version}
Provides:       tex(uwmj76.vf) = %{tl_version}, tex(uwmj77.vf) = %{tl_version}
Provides:       tex(uwmj78.vf) = %{tl_version}, tex(uwmj79.vf) = %{tl_version}
Provides:       tex(uwmj7a.vf) = %{tl_version}, tex(uwmj7b.vf) = %{tl_version}
Provides:       tex(uwmj7c.vf) = %{tl_version}, tex(uwmj7d.vf) = %{tl_version}
Provides:       tex(uwmj7e.vf) = %{tl_version}, tex(uwmj7f.vf) = %{tl_version}
Provides:       tex(uwmj80.vf) = %{tl_version}, tex(uwmj81.vf) = %{tl_version}
Provides:       tex(uwmj82.vf) = %{tl_version}, tex(uwmj83.vf) = %{tl_version}
Provides:       tex(uwmj84.vf) = %{tl_version}, tex(uwmj85.vf) = %{tl_version}
Provides:       tex(uwmj86.vf) = %{tl_version}, tex(uwmj87.vf) = %{tl_version}
Provides:       tex(uwmj88.vf) = %{tl_version}, tex(uwmj89.vf) = %{tl_version}
Provides:       tex(uwmj8a.vf) = %{tl_version}, tex(uwmj8b.vf) = %{tl_version}
Provides:       tex(uwmj8c.vf) = %{tl_version}, tex(uwmj8d.vf) = %{tl_version}
Provides:       tex(uwmj8e.vf) = %{tl_version}, tex(uwmj8f.vf) = %{tl_version}
Provides:       tex(uwmj90.vf) = %{tl_version}, tex(uwmj91.vf) = %{tl_version}
Provides:       tex(uwmj92.vf) = %{tl_version}, tex(uwmj93.vf) = %{tl_version}
Provides:       tex(uwmj94.vf) = %{tl_version}, tex(uwmj95.vf) = %{tl_version}
Provides:       tex(uwmj96.vf) = %{tl_version}, tex(uwmj97.vf) = %{tl_version}
Provides:       tex(uwmj98.vf) = %{tl_version}, tex(uwmj99.vf) = %{tl_version}
Provides:       tex(uwmj9a.vf) = %{tl_version}, tex(uwmj9b.vf) = %{tl_version}
Provides:       tex(uwmj9c.vf) = %{tl_version}, tex(uwmj9d.vf) = %{tl_version}
Provides:       tex(uwmj9e.vf) = %{tl_version}, tex(uwmj9f.vf) = %{tl_version}
Provides:       tex(uwmjac.vf) = %{tl_version}, tex(uwmjad.vf) = %{tl_version}
Provides:       tex(uwmjae.vf) = %{tl_version}, tex(uwmjaf.vf) = %{tl_version}
Provides:       tex(uwmjb0.vf) = %{tl_version}, tex(uwmjb1.vf) = %{tl_version}
Provides:       tex(uwmjb2.vf) = %{tl_version}, tex(uwmjb3.vf) = %{tl_version}
Provides:       tex(uwmjb4.vf) = %{tl_version}, tex(uwmjb5.vf) = %{tl_version}
Provides:       tex(uwmjb6.vf) = %{tl_version}, tex(uwmjb7.vf) = %{tl_version}
Provides:       tex(uwmjb8.vf) = %{tl_version}, tex(uwmjb9.vf) = %{tl_version}
Provides:       tex(uwmjba.vf) = %{tl_version}, tex(uwmjbb.vf) = %{tl_version}
Provides:       tex(uwmjbc.vf) = %{tl_version}, tex(uwmjbd.vf) = %{tl_version}
Provides:       tex(uwmjbe.vf) = %{tl_version}, tex(uwmjbf.vf) = %{tl_version}
Provides:       tex(uwmjc0.vf) = %{tl_version}, tex(uwmjc00.vf) = %{tl_version}
Provides:       tex(uwmjc01.vf) = %{tl_version}, tex(uwmjc02.vf) = %{tl_version}
Provides:       tex(uwmjc03.vf) = %{tl_version}, tex(uwmjc04.vf) = %{tl_version}
Provides:       tex(uwmjc1.vf) = %{tl_version}, tex(uwmjc2.vf) = %{tl_version}
Provides:       tex(uwmjc20.vf) = %{tl_version}, tex(uwmjc21.vf) = %{tl_version}
Provides:       tex(uwmjc22.vf) = %{tl_version}, tex(uwmjc23.vf) = %{tl_version}
Provides:       tex(uwmjc24.vf) = %{tl_version}, tex(uwmjc25.vf) = %{tl_version}
Provides:       tex(uwmjc26.vf) = %{tl_version}, tex(uwmjc3.vf) = %{tl_version}
Provides:       tex(uwmjc30.vf) = %{tl_version}, tex(uwmjc31.vf) = %{tl_version}
Provides:       tex(uwmjc32.vf) = %{tl_version}, tex(uwmjc33.vf) = %{tl_version}
Provides:       tex(uwmjc4.vf) = %{tl_version}, tex(uwmjc4e.vf) = %{tl_version}
Provides:       tex(uwmjc4f.vf) = %{tl_version}, tex(uwmjc5.vf) = %{tl_version}
Provides:       tex(uwmjc50.vf) = %{tl_version}, tex(uwmjc51.vf) = %{tl_version}
Provides:       tex(uwmjc52.vf) = %{tl_version}, tex(uwmjc53.vf) = %{tl_version}
Provides:       tex(uwmjc54.vf) = %{tl_version}, tex(uwmjc55.vf) = %{tl_version}
Provides:       tex(uwmjc56.vf) = %{tl_version}, tex(uwmjc57.vf) = %{tl_version}
Provides:       tex(uwmjc58.vf) = %{tl_version}, tex(uwmjc59.vf) = %{tl_version}
Provides:       tex(uwmjc5a.vf) = %{tl_version}, tex(uwmjc5b.vf) = %{tl_version}
Provides:       tex(uwmjc5c.vf) = %{tl_version}, tex(uwmjc5d.vf) = %{tl_version}
Provides:       tex(uwmjc5e.vf) = %{tl_version}, tex(uwmjc5f.vf) = %{tl_version}
Provides:       tex(uwmjc6.vf) = %{tl_version}, tex(uwmjc60.vf) = %{tl_version}
Provides:       tex(uwmjc61.vf) = %{tl_version}, tex(uwmjc62.vf) = %{tl_version}
Provides:       tex(uwmjc63.vf) = %{tl_version}, tex(uwmjc64.vf) = %{tl_version}
Provides:       tex(uwmjc65.vf) = %{tl_version}, tex(uwmjc66.vf) = %{tl_version}
Provides:       tex(uwmjc67.vf) = %{tl_version}, tex(uwmjc68.vf) = %{tl_version}
Provides:       tex(uwmjc69.vf) = %{tl_version}, tex(uwmjc6a.vf) = %{tl_version}
Provides:       tex(uwmjc6b.vf) = %{tl_version}, tex(uwmjc6c.vf) = %{tl_version}
Provides:       tex(uwmjc6d.vf) = %{tl_version}, tex(uwmjc6e.vf) = %{tl_version}
Provides:       tex(uwmjc6f.vf) = %{tl_version}, tex(uwmjc7.vf) = %{tl_version}
Provides:       tex(uwmjc70.vf) = %{tl_version}, tex(uwmjc71.vf) = %{tl_version}
Provides:       tex(uwmjc72.vf) = %{tl_version}, tex(uwmjc73.vf) = %{tl_version}
Provides:       tex(uwmjc74.vf) = %{tl_version}, tex(uwmjc75.vf) = %{tl_version}
Provides:       tex(uwmjc76.vf) = %{tl_version}, tex(uwmjc77.vf) = %{tl_version}
Provides:       tex(uwmjc78.vf) = %{tl_version}, tex(uwmjc79.vf) = %{tl_version}
Provides:       tex(uwmjc7a.vf) = %{tl_version}, tex(uwmjc7b.vf) = %{tl_version}
Provides:       tex(uwmjc7c.vf) = %{tl_version}, tex(uwmjc7d.vf) = %{tl_version}
Provides:       tex(uwmjc7e.vf) = %{tl_version}, tex(uwmjc7f.vf) = %{tl_version}
Provides:       tex(uwmjc8.vf) = %{tl_version}, tex(uwmjc80.vf) = %{tl_version}
Provides:       tex(uwmjc81.vf) = %{tl_version}, tex(uwmjc82.vf) = %{tl_version}
Provides:       tex(uwmjc83.vf) = %{tl_version}, tex(uwmjc84.vf) = %{tl_version}
Provides:       tex(uwmjc85.vf) = %{tl_version}, tex(uwmjc86.vf) = %{tl_version}
Provides:       tex(uwmjc87.vf) = %{tl_version}, tex(uwmjc88.vf) = %{tl_version}
Provides:       tex(uwmjc89.vf) = %{tl_version}, tex(uwmjc8a.vf) = %{tl_version}
Provides:       tex(uwmjc8b.vf) = %{tl_version}, tex(uwmjc8c.vf) = %{tl_version}
Provides:       tex(uwmjc8d.vf) = %{tl_version}, tex(uwmjc8e.vf) = %{tl_version}
Provides:       tex(uwmjc8f.vf) = %{tl_version}, tex(uwmjc9.vf) = %{tl_version}
Provides:       tex(uwmjc90.vf) = %{tl_version}, tex(uwmjc91.vf) = %{tl_version}
Provides:       tex(uwmjc92.vf) = %{tl_version}, tex(uwmjc93.vf) = %{tl_version}
Provides:       tex(uwmjc94.vf) = %{tl_version}, tex(uwmjc95.vf) = %{tl_version}
Provides:       tex(uwmjc96.vf) = %{tl_version}, tex(uwmjc97.vf) = %{tl_version}
Provides:       tex(uwmjc98.vf) = %{tl_version}, tex(uwmjc99.vf) = %{tl_version}
Provides:       tex(uwmjc9a.vf) = %{tl_version}, tex(uwmjc9b.vf) = %{tl_version}
Provides:       tex(uwmjc9c.vf) = %{tl_version}, tex(uwmjc9d.vf) = %{tl_version}
Provides:       tex(uwmjc9e.vf) = %{tl_version}, tex(uwmjc9f.vf) = %{tl_version}
Provides:       tex(uwmjca.vf) = %{tl_version}, tex(uwmjcac.vf) = %{tl_version}
Provides:       tex(uwmjcad.vf) = %{tl_version}, tex(uwmjcae.vf) = %{tl_version}
Provides:       tex(uwmjcaf.vf) = %{tl_version}, tex(uwmjcb.vf) = %{tl_version}
Provides:       tex(uwmjcb0.vf) = %{tl_version}, tex(uwmjcb1.vf) = %{tl_version}
Provides:       tex(uwmjcb2.vf) = %{tl_version}, tex(uwmjcb3.vf) = %{tl_version}
Provides:       tex(uwmjcb4.vf) = %{tl_version}, tex(uwmjcb5.vf) = %{tl_version}
Provides:       tex(uwmjcb6.vf) = %{tl_version}, tex(uwmjcb7.vf) = %{tl_version}
Provides:       tex(uwmjcb8.vf) = %{tl_version}, tex(uwmjcb9.vf) = %{tl_version}
Provides:       tex(uwmjcba.vf) = %{tl_version}, tex(uwmjcbb.vf) = %{tl_version}
Provides:       tex(uwmjcbc.vf) = %{tl_version}, tex(uwmjcbd.vf) = %{tl_version}
Provides:       tex(uwmjcbe.vf) = %{tl_version}, tex(uwmjcbf.vf) = %{tl_version}
Provides:       tex(uwmjcc.vf) = %{tl_version}, tex(uwmjcc0.vf) = %{tl_version}
Provides:       tex(uwmjcc1.vf) = %{tl_version}, tex(uwmjcc2.vf) = %{tl_version}
Provides:       tex(uwmjcc3.vf) = %{tl_version}, tex(uwmjcc4.vf) = %{tl_version}
Provides:       tex(uwmjcc5.vf) = %{tl_version}, tex(uwmjcc6.vf) = %{tl_version}
Provides:       tex(uwmjcc7.vf) = %{tl_version}, tex(uwmjcc8.vf) = %{tl_version}
Provides:       tex(uwmjcc9.vf) = %{tl_version}, tex(uwmjcca.vf) = %{tl_version}
Provides:       tex(uwmjccb.vf) = %{tl_version}, tex(uwmjccc.vf) = %{tl_version}
Provides:       tex(uwmjccd.vf) = %{tl_version}, tex(uwmjcce.vf) = %{tl_version}
Provides:       tex(uwmjccf.vf) = %{tl_version}, tex(uwmjcd.vf) = %{tl_version}
Provides:       tex(uwmjcd0.vf) = %{tl_version}, tex(uwmjcd1.vf) = %{tl_version}
Provides:       tex(uwmjcd2.vf) = %{tl_version}, tex(uwmjcd3.vf) = %{tl_version}
Provides:       tex(uwmjcd4.vf) = %{tl_version}, tex(uwmjcd5.vf) = %{tl_version}
Provides:       tex(uwmjcd6.vf) = %{tl_version}, tex(uwmjcd7.vf) = %{tl_version}
Provides:       tex(uwmjce.vf) = %{tl_version}, tex(uwmjcf.vf) = %{tl_version}
Provides:       tex(uwmjcf9.vf) = %{tl_version}, tex(uwmjcfa.vf) = %{tl_version}
Provides:       tex(uwmjcff.vf) = %{tl_version}, tex(uwmjco00.vf) = %{tl_version}
Provides:       tex(uwmjco01.vf) = %{tl_version}, tex(uwmjco02.vf) = %{tl_version}
Provides:       tex(uwmjco03.vf) = %{tl_version}, tex(uwmjco04.vf) = %{tl_version}
Provides:       tex(uwmjco20.vf) = %{tl_version}, tex(uwmjco21.vf) = %{tl_version}
Provides:       tex(uwmjco22.vf) = %{tl_version}, tex(uwmjco23.vf) = %{tl_version}
Provides:       tex(uwmjco24.vf) = %{tl_version}, tex(uwmjco25.vf) = %{tl_version}
Provides:       tex(uwmjco26.vf) = %{tl_version}, tex(uwmjco30.vf) = %{tl_version}
Provides:       tex(uwmjco31.vf) = %{tl_version}, tex(uwmjco32.vf) = %{tl_version}
Provides:       tex(uwmjco33.vf) = %{tl_version}, tex(uwmjco4e.vf) = %{tl_version}
Provides:       tex(uwmjco4f.vf) = %{tl_version}, tex(uwmjco50.vf) = %{tl_version}
Provides:       tex(uwmjco51.vf) = %{tl_version}, tex(uwmjco52.vf) = %{tl_version}
Provides:       tex(uwmjco53.vf) = %{tl_version}, tex(uwmjco54.vf) = %{tl_version}
Provides:       tex(uwmjco55.vf) = %{tl_version}, tex(uwmjco56.vf) = %{tl_version}
Provides:       tex(uwmjco57.vf) = %{tl_version}, tex(uwmjco58.vf) = %{tl_version}
Provides:       tex(uwmjco59.vf) = %{tl_version}, tex(uwmjco5a.vf) = %{tl_version}
Provides:       tex(uwmjco5b.vf) = %{tl_version}, tex(uwmjco5c.vf) = %{tl_version}
Provides:       tex(uwmjco5d.vf) = %{tl_version}, tex(uwmjco5e.vf) = %{tl_version}
Provides:       tex(uwmjco5f.vf) = %{tl_version}, tex(uwmjco60.vf) = %{tl_version}
Provides:       tex(uwmjco61.vf) = %{tl_version}, tex(uwmjco62.vf) = %{tl_version}
Provides:       tex(uwmjco63.vf) = %{tl_version}, tex(uwmjco64.vf) = %{tl_version}
Provides:       tex(uwmjco65.vf) = %{tl_version}, tex(uwmjco66.vf) = %{tl_version}
Provides:       tex(uwmjco67.vf) = %{tl_version}, tex(uwmjco68.vf) = %{tl_version}
Provides:       tex(uwmjco69.vf) = %{tl_version}, tex(uwmjco6a.vf) = %{tl_version}
Provides:       tex(uwmjco6b.vf) = %{tl_version}, tex(uwmjco6c.vf) = %{tl_version}
Provides:       tex(uwmjco6d.vf) = %{tl_version}, tex(uwmjco6e.vf) = %{tl_version}
Provides:       tex(uwmjco6f.vf) = %{tl_version}, tex(uwmjco70.vf) = %{tl_version}
Provides:       tex(uwmjco71.vf) = %{tl_version}, tex(uwmjco72.vf) = %{tl_version}
Provides:       tex(uwmjco73.vf) = %{tl_version}, tex(uwmjco74.vf) = %{tl_version}
Provides:       tex(uwmjco75.vf) = %{tl_version}, tex(uwmjco76.vf) = %{tl_version}
Provides:       tex(uwmjco77.vf) = %{tl_version}, tex(uwmjco78.vf) = %{tl_version}
Provides:       tex(uwmjco79.vf) = %{tl_version}, tex(uwmjco7a.vf) = %{tl_version}
Provides:       tex(uwmjco7b.vf) = %{tl_version}, tex(uwmjco7c.vf) = %{tl_version}
Provides:       tex(uwmjco7d.vf) = %{tl_version}, tex(uwmjco7e.vf) = %{tl_version}
Provides:       tex(uwmjco7f.vf) = %{tl_version}, tex(uwmjco80.vf) = %{tl_version}
Provides:       tex(uwmjco81.vf) = %{tl_version}, tex(uwmjco82.vf) = %{tl_version}
Provides:       tex(uwmjco83.vf) = %{tl_version}, tex(uwmjco84.vf) = %{tl_version}
Provides:       tex(uwmjco85.vf) = %{tl_version}, tex(uwmjco86.vf) = %{tl_version}
Provides:       tex(uwmjco87.vf) = %{tl_version}, tex(uwmjco88.vf) = %{tl_version}
Provides:       tex(uwmjco89.vf) = %{tl_version}, tex(uwmjco8a.vf) = %{tl_version}
Provides:       tex(uwmjco8b.vf) = %{tl_version}, tex(uwmjco8c.vf) = %{tl_version}
Provides:       tex(uwmjco8d.vf) = %{tl_version}, tex(uwmjco8e.vf) = %{tl_version}
Provides:       tex(uwmjco8f.vf) = %{tl_version}, tex(uwmjco90.vf) = %{tl_version}
Provides:       tex(uwmjco91.vf) = %{tl_version}, tex(uwmjco92.vf) = %{tl_version}
Provides:       tex(uwmjco93.vf) = %{tl_version}, tex(uwmjco94.vf) = %{tl_version}
Provides:       tex(uwmjco95.vf) = %{tl_version}, tex(uwmjco96.vf) = %{tl_version}
Provides:       tex(uwmjco97.vf) = %{tl_version}, tex(uwmjco98.vf) = %{tl_version}
Provides:       tex(uwmjco99.vf) = %{tl_version}, tex(uwmjco9a.vf) = %{tl_version}
Provides:       tex(uwmjco9b.vf) = %{tl_version}, tex(uwmjco9c.vf) = %{tl_version}
Provides:       tex(uwmjco9d.vf) = %{tl_version}, tex(uwmjco9e.vf) = %{tl_version}
Provides:       tex(uwmjco9f.vf) = %{tl_version}, tex(uwmjcoac.vf) = %{tl_version}
Provides:       tex(uwmjcoad.vf) = %{tl_version}, tex(uwmjcoae.vf) = %{tl_version}
Provides:       tex(uwmjcoaf.vf) = %{tl_version}, tex(uwmjcob0.vf) = %{tl_version}
Provides:       tex(uwmjcob1.vf) = %{tl_version}, tex(uwmjcob2.vf) = %{tl_version}
Provides:       tex(uwmjcob3.vf) = %{tl_version}, tex(uwmjcob4.vf) = %{tl_version}
Provides:       tex(uwmjcob5.vf) = %{tl_version}, tex(uwmjcob6.vf) = %{tl_version}
Provides:       tex(uwmjcob7.vf) = %{tl_version}, tex(uwmjcob8.vf) = %{tl_version}
Provides:       tex(uwmjcob9.vf) = %{tl_version}, tex(uwmjcoba.vf) = %{tl_version}
Provides:       tex(uwmjcobb.vf) = %{tl_version}, tex(uwmjcobc.vf) = %{tl_version}
Provides:       tex(uwmjcobd.vf) = %{tl_version}, tex(uwmjcobe.vf) = %{tl_version}
Provides:       tex(uwmjcobf.vf) = %{tl_version}, tex(uwmjcoc0.vf) = %{tl_version}
Provides:       tex(uwmjcoc1.vf) = %{tl_version}, tex(uwmjcoc2.vf) = %{tl_version}
Provides:       tex(uwmjcoc3.vf) = %{tl_version}, tex(uwmjcoc4.vf) = %{tl_version}
Provides:       tex(uwmjcoc5.vf) = %{tl_version}, tex(uwmjcoc6.vf) = %{tl_version}
Provides:       tex(uwmjcoc7.vf) = %{tl_version}, tex(uwmjcoc8.vf) = %{tl_version}
Provides:       tex(uwmjcoc9.vf) = %{tl_version}, tex(uwmjcoca.vf) = %{tl_version}
Provides:       tex(uwmjcocb.vf) = %{tl_version}, tex(uwmjcocc.vf) = %{tl_version}
Provides:       tex(uwmjcocd.vf) = %{tl_version}, tex(uwmjcoce.vf) = %{tl_version}
Provides:       tex(uwmjcocf.vf) = %{tl_version}, tex(uwmjcod0.vf) = %{tl_version}
Provides:       tex(uwmjcod1.vf) = %{tl_version}, tex(uwmjcod2.vf) = %{tl_version}
Provides:       tex(uwmjcod3.vf) = %{tl_version}, tex(uwmjcod4.vf) = %{tl_version}
Provides:       tex(uwmjcod5.vf) = %{tl_version}, tex(uwmjcod6.vf) = %{tl_version}
Provides:       tex(uwmjcod7.vf) = %{tl_version}, tex(uwmjcof9.vf) = %{tl_version}
Provides:       tex(uwmjcofa.vf) = %{tl_version}, tex(uwmjcoff.vf) = %{tl_version}
Provides:       tex(uwmjd0.vf) = %{tl_version}, tex(uwmjd1.vf) = %{tl_version}
Provides:       tex(uwmjd2.vf) = %{tl_version}, tex(uwmjd3.vf) = %{tl_version}
Provides:       tex(uwmjd4.vf) = %{tl_version}, tex(uwmjd5.vf) = %{tl_version}
Provides:       tex(uwmjd6.vf) = %{tl_version}, tex(uwmjd7.vf) = %{tl_version}
Provides:       tex(uwmjf9.vf) = %{tl_version}, tex(uwmjfa.vf) = %{tl_version}
Provides:       tex(uwmjff.vf) = %{tl_version}, tex(uwmjo00.vf) = %{tl_version}
Provides:       tex(uwmjo01.vf) = %{tl_version}, tex(uwmjo02.vf) = %{tl_version}
Provides:       tex(uwmjo03.vf) = %{tl_version}, tex(uwmjo04.vf) = %{tl_version}
Provides:       tex(uwmjo20.vf) = %{tl_version}, tex(uwmjo21.vf) = %{tl_version}
Provides:       tex(uwmjo22.vf) = %{tl_version}, tex(uwmjo23.vf) = %{tl_version}
Provides:       tex(uwmjo24.vf) = %{tl_version}, tex(uwmjo25.vf) = %{tl_version}
Provides:       tex(uwmjo26.vf) = %{tl_version}, tex(uwmjo30.vf) = %{tl_version}
Provides:       tex(uwmjo31.vf) = %{tl_version}, tex(uwmjo32.vf) = %{tl_version}
Provides:       tex(uwmjo33.vf) = %{tl_version}, tex(uwmjo4e.vf) = %{tl_version}
Provides:       tex(uwmjo4f.vf) = %{tl_version}, tex(uwmjo50.vf) = %{tl_version}
Provides:       tex(uwmjo51.vf) = %{tl_version}, tex(uwmjo52.vf) = %{tl_version}
Provides:       tex(uwmjo53.vf) = %{tl_version}, tex(uwmjo54.vf) = %{tl_version}
Provides:       tex(uwmjo55.vf) = %{tl_version}, tex(uwmjo56.vf) = %{tl_version}
Provides:       tex(uwmjo57.vf) = %{tl_version}, tex(uwmjo58.vf) = %{tl_version}
Provides:       tex(uwmjo59.vf) = %{tl_version}, tex(uwmjo5a.vf) = %{tl_version}
Provides:       tex(uwmjo5b.vf) = %{tl_version}, tex(uwmjo5c.vf) = %{tl_version}
Provides:       tex(uwmjo5d.vf) = %{tl_version}, tex(uwmjo5e.vf) = %{tl_version}
Provides:       tex(uwmjo5f.vf) = %{tl_version}, tex(uwmjo60.vf) = %{tl_version}
Provides:       tex(uwmjo61.vf) = %{tl_version}, tex(uwmjo62.vf) = %{tl_version}
Provides:       tex(uwmjo63.vf) = %{tl_version}, tex(uwmjo64.vf) = %{tl_version}
Provides:       tex(uwmjo65.vf) = %{tl_version}, tex(uwmjo66.vf) = %{tl_version}
Provides:       tex(uwmjo67.vf) = %{tl_version}, tex(uwmjo68.vf) = %{tl_version}
Provides:       tex(uwmjo69.vf) = %{tl_version}, tex(uwmjo6a.vf) = %{tl_version}
Provides:       tex(uwmjo6b.vf) = %{tl_version}, tex(uwmjo6c.vf) = %{tl_version}
Provides:       tex(uwmjo6d.vf) = %{tl_version}, tex(uwmjo6e.vf) = %{tl_version}
Provides:       tex(uwmjo6f.vf) = %{tl_version}, tex(uwmjo70.vf) = %{tl_version}
Provides:       tex(uwmjo71.vf) = %{tl_version}, tex(uwmjo72.vf) = %{tl_version}
Provides:       tex(uwmjo73.vf) = %{tl_version}, tex(uwmjo74.vf) = %{tl_version}
Provides:       tex(uwmjo75.vf) = %{tl_version}, tex(uwmjo76.vf) = %{tl_version}
Provides:       tex(uwmjo77.vf) = %{tl_version}, tex(uwmjo78.vf) = %{tl_version}
Provides:       tex(uwmjo79.vf) = %{tl_version}, tex(uwmjo7a.vf) = %{tl_version}
Provides:       tex(uwmjo7b.vf) = %{tl_version}, tex(uwmjo7c.vf) = %{tl_version}
Provides:       tex(uwmjo7d.vf) = %{tl_version}, tex(uwmjo7e.vf) = %{tl_version}
Provides:       tex(uwmjo7f.vf) = %{tl_version}, tex(uwmjo80.vf) = %{tl_version}
Provides:       tex(uwmjo81.vf) = %{tl_version}, tex(uwmjo82.vf) = %{tl_version}
Provides:       tex(uwmjo83.vf) = %{tl_version}, tex(uwmjo84.vf) = %{tl_version}
Provides:       tex(uwmjo85.vf) = %{tl_version}, tex(uwmjo86.vf) = %{tl_version}
Provides:       tex(uwmjo87.vf) = %{tl_version}, tex(uwmjo88.vf) = %{tl_version}
Provides:       tex(uwmjo89.vf) = %{tl_version}, tex(uwmjo8a.vf) = %{tl_version}
Provides:       tex(uwmjo8b.vf) = %{tl_version}, tex(uwmjo8c.vf) = %{tl_version}
Provides:       tex(uwmjo8d.vf) = %{tl_version}, tex(uwmjo8e.vf) = %{tl_version}
Provides:       tex(uwmjo8f.vf) = %{tl_version}, tex(uwmjo90.vf) = %{tl_version}
Provides:       tex(uwmjo91.vf) = %{tl_version}, tex(uwmjo92.vf) = %{tl_version}
Provides:       tex(uwmjo93.vf) = %{tl_version}, tex(uwmjo94.vf) = %{tl_version}
Provides:       tex(uwmjo95.vf) = %{tl_version}, tex(uwmjo96.vf) = %{tl_version}
Provides:       tex(uwmjo97.vf) = %{tl_version}, tex(uwmjo98.vf) = %{tl_version}
Provides:       tex(uwmjo99.vf) = %{tl_version}, tex(uwmjo9a.vf) = %{tl_version}
Provides:       tex(uwmjo9b.vf) = %{tl_version}, tex(uwmjo9c.vf) = %{tl_version}
Provides:       tex(uwmjo9d.vf) = %{tl_version}, tex(uwmjo9e.vf) = %{tl_version}
Provides:       tex(uwmjo9f.vf) = %{tl_version}, tex(uwmjoac.vf) = %{tl_version}
Provides:       tex(uwmjoad.vf) = %{tl_version}, tex(uwmjoae.vf) = %{tl_version}
Provides:       tex(uwmjoaf.vf) = %{tl_version}, tex(uwmjob0.vf) = %{tl_version}
Provides:       tex(uwmjob1.vf) = %{tl_version}, tex(uwmjob2.vf) = %{tl_version}
Provides:       tex(uwmjob3.vf) = %{tl_version}, tex(uwmjob4.vf) = %{tl_version}
Provides:       tex(uwmjob5.vf) = %{tl_version}, tex(uwmjob6.vf) = %{tl_version}
Provides:       tex(uwmjob7.vf) = %{tl_version}, tex(uwmjob8.vf) = %{tl_version}
Provides:       tex(uwmjob9.vf) = %{tl_version}, tex(uwmjoba.vf) = %{tl_version}
Provides:       tex(uwmjobb.vf) = %{tl_version}, tex(uwmjobc.vf) = %{tl_version}
Provides:       tex(uwmjobd.vf) = %{tl_version}, tex(uwmjobe.vf) = %{tl_version}
Provides:       tex(uwmjobf.vf) = %{tl_version}, tex(uwmjoc0.vf) = %{tl_version}
Provides:       tex(uwmjoc1.vf) = %{tl_version}, tex(uwmjoc2.vf) = %{tl_version}
Provides:       tex(uwmjoc3.vf) = %{tl_version}, tex(uwmjoc4.vf) = %{tl_version}
Provides:       tex(uwmjoc5.vf) = %{tl_version}, tex(uwmjoc6.vf) = %{tl_version}
Provides:       tex(uwmjoc7.vf) = %{tl_version}, tex(uwmjoc8.vf) = %{tl_version}
Provides:       tex(uwmjoc9.vf) = %{tl_version}, tex(uwmjoca.vf) = %{tl_version}
Provides:       tex(uwmjocb.vf) = %{tl_version}, tex(uwmjocc.vf) = %{tl_version}
Provides:       tex(uwmjocd.vf) = %{tl_version}, tex(uwmjoce.vf) = %{tl_version}
Provides:       tex(uwmjocf.vf) = %{tl_version}, tex(uwmjod0.vf) = %{tl_version}
Provides:       tex(uwmjod1.vf) = %{tl_version}, tex(uwmjod2.vf) = %{tl_version}
Provides:       tex(uwmjod3.vf) = %{tl_version}, tex(uwmjod4.vf) = %{tl_version}
Provides:       tex(uwmjod5.vf) = %{tl_version}, tex(uwmjod6.vf) = %{tl_version}
Provides:       tex(uwmjod7.vf) = %{tl_version}, tex(uwmjof9.vf) = %{tl_version}
Provides:       tex(uwmjofa.vf) = %{tl_version}, tex(uwmjoff.vf) = %{tl_version}
Provides:       tex(uwmju00.vf) = %{tl_version}, tex(uwmju01.vf) = %{tl_version}
Provides:       tex(uwmju02.vf) = %{tl_version}, tex(uwmju03.vf) = %{tl_version}
Provides:       tex(uwmju04.vf) = %{tl_version}, tex(uwmju20.vf) = %{tl_version}
Provides:       tex(uwmju21.vf) = %{tl_version}, tex(uwmju22.vf) = %{tl_version}
Provides:       tex(uwmju23.vf) = %{tl_version}, tex(uwmju24.vf) = %{tl_version}
Provides:       tex(uwmju25.vf) = %{tl_version}, tex(uwmju26.vf) = %{tl_version}
Provides:       tex(uwmju30.vf) = %{tl_version}, tex(uwmju31.vf) = %{tl_version}
Provides:       tex(uwmju32.vf) = %{tl_version}, tex(uwmju33.vf) = %{tl_version}
Provides:       tex(uwmju4e.vf) = %{tl_version}, tex(uwmju4f.vf) = %{tl_version}
Provides:       tex(uwmju50.vf) = %{tl_version}, tex(uwmju51.vf) = %{tl_version}
Provides:       tex(uwmju52.vf) = %{tl_version}, tex(uwmju53.vf) = %{tl_version}
Provides:       tex(uwmju54.vf) = %{tl_version}, tex(uwmju55.vf) = %{tl_version}
Provides:       tex(uwmju56.vf) = %{tl_version}, tex(uwmju57.vf) = %{tl_version}
Provides:       tex(uwmju58.vf) = %{tl_version}, tex(uwmju59.vf) = %{tl_version}
Provides:       tex(uwmju5a.vf) = %{tl_version}, tex(uwmju5b.vf) = %{tl_version}
Provides:       tex(uwmju5c.vf) = %{tl_version}, tex(uwmju5d.vf) = %{tl_version}
Provides:       tex(uwmju5e.vf) = %{tl_version}, tex(uwmju5f.vf) = %{tl_version}
Provides:       tex(uwmju60.vf) = %{tl_version}, tex(uwmju61.vf) = %{tl_version}
Provides:       tex(uwmju62.vf) = %{tl_version}, tex(uwmju63.vf) = %{tl_version}
Provides:       tex(uwmju64.vf) = %{tl_version}, tex(uwmju65.vf) = %{tl_version}
Provides:       tex(uwmju66.vf) = %{tl_version}, tex(uwmju67.vf) = %{tl_version}
Provides:       tex(uwmju68.vf) = %{tl_version}, tex(uwmju69.vf) = %{tl_version}
Provides:       tex(uwmju6a.vf) = %{tl_version}, tex(uwmju6b.vf) = %{tl_version}
Provides:       tex(uwmju6c.vf) = %{tl_version}, tex(uwmju6d.vf) = %{tl_version}
Provides:       tex(uwmju6e.vf) = %{tl_version}, tex(uwmju6f.vf) = %{tl_version}
Provides:       tex(uwmju70.vf) = %{tl_version}, tex(uwmju71.vf) = %{tl_version}
Provides:       tex(uwmju72.vf) = %{tl_version}, tex(uwmju73.vf) = %{tl_version}
Provides:       tex(uwmju74.vf) = %{tl_version}, tex(uwmju75.vf) = %{tl_version}
Provides:       tex(uwmju76.vf) = %{tl_version}, tex(uwmju77.vf) = %{tl_version}
Provides:       tex(uwmju78.vf) = %{tl_version}, tex(uwmju79.vf) = %{tl_version}
Provides:       tex(uwmju7a.vf) = %{tl_version}, tex(uwmju7b.vf) = %{tl_version}
Provides:       tex(uwmju7c.vf) = %{tl_version}, tex(uwmju7d.vf) = %{tl_version}
Provides:       tex(uwmju7e.vf) = %{tl_version}, tex(uwmju7f.vf) = %{tl_version}
Provides:       tex(uwmju80.vf) = %{tl_version}, tex(uwmju81.vf) = %{tl_version}
Provides:       tex(uwmju82.vf) = %{tl_version}, tex(uwmju83.vf) = %{tl_version}
Provides:       tex(uwmju84.vf) = %{tl_version}, tex(uwmju85.vf) = %{tl_version}
Provides:       tex(uwmju86.vf) = %{tl_version}, tex(uwmju87.vf) = %{tl_version}
Provides:       tex(uwmju88.vf) = %{tl_version}, tex(uwmju89.vf) = %{tl_version}
Provides:       tex(uwmju8a.vf) = %{tl_version}, tex(uwmju8b.vf) = %{tl_version}
Provides:       tex(uwmju8c.vf) = %{tl_version}, tex(uwmju8d.vf) = %{tl_version}
Provides:       tex(uwmju8e.vf) = %{tl_version}, tex(uwmju8f.vf) = %{tl_version}
Provides:       tex(uwmju90.vf) = %{tl_version}, tex(uwmju91.vf) = %{tl_version}
Provides:       tex(uwmju92.vf) = %{tl_version}, tex(uwmju93.vf) = %{tl_version}
Provides:       tex(uwmju94.vf) = %{tl_version}, tex(uwmju95.vf) = %{tl_version}
Provides:       tex(uwmju96.vf) = %{tl_version}, tex(uwmju97.vf) = %{tl_version}
Provides:       tex(uwmju98.vf) = %{tl_version}, tex(uwmju99.vf) = %{tl_version}
Provides:       tex(uwmju9a.vf) = %{tl_version}, tex(uwmju9b.vf) = %{tl_version}
Provides:       tex(uwmju9c.vf) = %{tl_version}, tex(uwmju9d.vf) = %{tl_version}
Provides:       tex(uwmju9e.vf) = %{tl_version}, tex(uwmju9f.vf) = %{tl_version}
Provides:       tex(uwmjuac.vf) = %{tl_version}, tex(uwmjuad.vf) = %{tl_version}
Provides:       tex(uwmjuae.vf) = %{tl_version}, tex(uwmjuaf.vf) = %{tl_version}
Provides:       tex(uwmjub0.vf) = %{tl_version}, tex(uwmjub1.vf) = %{tl_version}
Provides:       tex(uwmjub2.vf) = %{tl_version}, tex(uwmjub3.vf) = %{tl_version}
Provides:       tex(uwmjub4.vf) = %{tl_version}, tex(uwmjub5.vf) = %{tl_version}
Provides:       tex(uwmjub6.vf) = %{tl_version}, tex(uwmjub7.vf) = %{tl_version}
Provides:       tex(uwmjub8.vf) = %{tl_version}, tex(uwmjub9.vf) = %{tl_version}
Provides:       tex(uwmjuba.vf) = %{tl_version}, tex(uwmjubb.vf) = %{tl_version}
Provides:       tex(uwmjubc.vf) = %{tl_version}, tex(uwmjubd.vf) = %{tl_version}
Provides:       tex(uwmjube.vf) = %{tl_version}, tex(uwmjubf.vf) = %{tl_version}
Provides:       tex(uwmjuc0.vf) = %{tl_version}, tex(uwmjuc1.vf) = %{tl_version}
Provides:       tex(uwmjuc2.vf) = %{tl_version}, tex(uwmjuc3.vf) = %{tl_version}
Provides:       tex(uwmjuc4.vf) = %{tl_version}, tex(uwmjuc5.vf) = %{tl_version}
Provides:       tex(uwmjuc6.vf) = %{tl_version}, tex(uwmjuc7.vf) = %{tl_version}
Provides:       tex(uwmjuc8.vf) = %{tl_version}, tex(uwmjuc9.vf) = %{tl_version}
Provides:       tex(uwmjuca.vf) = %{tl_version}, tex(uwmjucb.vf) = %{tl_version}
Provides:       tex(uwmjucc.vf) = %{tl_version}, tex(uwmjucd.vf) = %{tl_version}
Provides:       tex(uwmjuce.vf) = %{tl_version}, tex(uwmjucf.vf) = %{tl_version}
Provides:       tex(uwmjud0.vf) = %{tl_version}, tex(uwmjud1.vf) = %{tl_version}
Provides:       tex(uwmjud2.vf) = %{tl_version}, tex(uwmjud3.vf) = %{tl_version}
Provides:       tex(uwmjud4.vf) = %{tl_version}, tex(uwmjud5.vf) = %{tl_version}
Provides:       tex(uwmjud6.vf) = %{tl_version}, tex(uwmjud7.vf) = %{tl_version}
Provides:       tex(uwmjuf9.vf) = %{tl_version}, tex(uwmjufa.vf) = %{tl_version}
Provides:       tex(uwmjuff.vf) = %{tl_version}, tex(uwmjuo00.vf) = %{tl_version}
Provides:       tex(uwmjuo01.vf) = %{tl_version}, tex(uwmjuo02.vf) = %{tl_version}
Provides:       tex(uwmjuo03.vf) = %{tl_version}, tex(uwmjuo04.vf) = %{tl_version}
Provides:       tex(uwmjuo20.vf) = %{tl_version}, tex(uwmjuo21.vf) = %{tl_version}
Provides:       tex(uwmjuo22.vf) = %{tl_version}, tex(uwmjuo23.vf) = %{tl_version}
Provides:       tex(uwmjuo24.vf) = %{tl_version}, tex(uwmjuo25.vf) = %{tl_version}
Provides:       tex(uwmjuo26.vf) = %{tl_version}, tex(uwmjuo30.vf) = %{tl_version}
Provides:       tex(uwmjuo31.vf) = %{tl_version}, tex(uwmjuo32.vf) = %{tl_version}
Provides:       tex(uwmjuo33.vf) = %{tl_version}, tex(uwmjuo4e.vf) = %{tl_version}
Provides:       tex(uwmjuo4f.vf) = %{tl_version}, tex(uwmjuo50.vf) = %{tl_version}
Provides:       tex(uwmjuo51.vf) = %{tl_version}, tex(uwmjuo52.vf) = %{tl_version}
Provides:       tex(uwmjuo53.vf) = %{tl_version}, tex(uwmjuo54.vf) = %{tl_version}
Provides:       tex(uwmjuo55.vf) = %{tl_version}, tex(uwmjuo56.vf) = %{tl_version}
Provides:       tex(uwmjuo57.vf) = %{tl_version}, tex(uwmjuo58.vf) = %{tl_version}
Provides:       tex(uwmjuo59.vf) = %{tl_version}, tex(uwmjuo5a.vf) = %{tl_version}
Provides:       tex(uwmjuo5b.vf) = %{tl_version}, tex(uwmjuo5c.vf) = %{tl_version}
Provides:       tex(uwmjuo5d.vf) = %{tl_version}, tex(uwmjuo5e.vf) = %{tl_version}
Provides:       tex(uwmjuo5f.vf) = %{tl_version}, tex(uwmjuo60.vf) = %{tl_version}
Provides:       tex(uwmjuo61.vf) = %{tl_version}, tex(uwmjuo62.vf) = %{tl_version}
Provides:       tex(uwmjuo63.vf) = %{tl_version}, tex(uwmjuo64.vf) = %{tl_version}
Provides:       tex(uwmjuo65.vf) = %{tl_version}, tex(uwmjuo66.vf) = %{tl_version}
Provides:       tex(uwmjuo67.vf) = %{tl_version}, tex(uwmjuo68.vf) = %{tl_version}
Provides:       tex(uwmjuo69.vf) = %{tl_version}, tex(uwmjuo6a.vf) = %{tl_version}
Provides:       tex(uwmjuo6b.vf) = %{tl_version}, tex(uwmjuo6c.vf) = %{tl_version}
Provides:       tex(uwmjuo6d.vf) = %{tl_version}, tex(uwmjuo6e.vf) = %{tl_version}
Provides:       tex(uwmjuo6f.vf) = %{tl_version}, tex(uwmjuo70.vf) = %{tl_version}
Provides:       tex(uwmjuo71.vf) = %{tl_version}, tex(uwmjuo72.vf) = %{tl_version}
Provides:       tex(uwmjuo73.vf) = %{tl_version}, tex(uwmjuo74.vf) = %{tl_version}
Provides:       tex(uwmjuo75.vf) = %{tl_version}, tex(uwmjuo76.vf) = %{tl_version}
Provides:       tex(uwmjuo77.vf) = %{tl_version}, tex(uwmjuo78.vf) = %{tl_version}
Provides:       tex(uwmjuo79.vf) = %{tl_version}, tex(uwmjuo7a.vf) = %{tl_version}
Provides:       tex(uwmjuo7b.vf) = %{tl_version}, tex(uwmjuo7c.vf) = %{tl_version}
Provides:       tex(uwmjuo7d.vf) = %{tl_version}, tex(uwmjuo7e.vf) = %{tl_version}
Provides:       tex(uwmjuo7f.vf) = %{tl_version}, tex(uwmjuo80.vf) = %{tl_version}
Provides:       tex(uwmjuo81.vf) = %{tl_version}, tex(uwmjuo82.vf) = %{tl_version}
Provides:       tex(uwmjuo83.vf) = %{tl_version}, tex(uwmjuo84.vf) = %{tl_version}
Provides:       tex(uwmjuo85.vf) = %{tl_version}, tex(uwmjuo86.vf) = %{tl_version}
Provides:       tex(uwmjuo87.vf) = %{tl_version}, tex(uwmjuo88.vf) = %{tl_version}
Provides:       tex(uwmjuo89.vf) = %{tl_version}, tex(uwmjuo8a.vf) = %{tl_version}
Provides:       tex(uwmjuo8b.vf) = %{tl_version}, tex(uwmjuo8c.vf) = %{tl_version}
Provides:       tex(uwmjuo8d.vf) = %{tl_version}, tex(uwmjuo8e.vf) = %{tl_version}
Provides:       tex(uwmjuo8f.vf) = %{tl_version}, tex(uwmjuo90.vf) = %{tl_version}
Provides:       tex(uwmjuo91.vf) = %{tl_version}, tex(uwmjuo92.vf) = %{tl_version}
Provides:       tex(uwmjuo93.vf) = %{tl_version}, tex(uwmjuo94.vf) = %{tl_version}
Provides:       tex(uwmjuo95.vf) = %{tl_version}, tex(uwmjuo96.vf) = %{tl_version}
Provides:       tex(uwmjuo97.vf) = %{tl_version}, tex(uwmjuo98.vf) = %{tl_version}
Provides:       tex(uwmjuo99.vf) = %{tl_version}, tex(uwmjuo9a.vf) = %{tl_version}
Provides:       tex(uwmjuo9b.vf) = %{tl_version}, tex(uwmjuo9c.vf) = %{tl_version}
Provides:       tex(uwmjuo9d.vf) = %{tl_version}, tex(uwmjuo9e.vf) = %{tl_version}
Provides:       tex(uwmjuo9f.vf) = %{tl_version}, tex(uwmjuoac.vf) = %{tl_version}
Provides:       tex(uwmjuoad.vf) = %{tl_version}, tex(uwmjuoae.vf) = %{tl_version}
Provides:       tex(uwmjuoaf.vf) = %{tl_version}, tex(uwmjuob0.vf) = %{tl_version}
Provides:       tex(uwmjuob1.vf) = %{tl_version}, tex(uwmjuob2.vf) = %{tl_version}
Provides:       tex(uwmjuob3.vf) = %{tl_version}, tex(uwmjuob4.vf) = %{tl_version}
Provides:       tex(uwmjuob5.vf) = %{tl_version}, tex(uwmjuob6.vf) = %{tl_version}
Provides:       tex(uwmjuob7.vf) = %{tl_version}, tex(uwmjuob8.vf) = %{tl_version}
Provides:       tex(uwmjuob9.vf) = %{tl_version}, tex(uwmjuoba.vf) = %{tl_version}
Provides:       tex(uwmjuobb.vf) = %{tl_version}, tex(uwmjuobc.vf) = %{tl_version}
Provides:       tex(uwmjuobd.vf) = %{tl_version}, tex(uwmjuobe.vf) = %{tl_version}
Provides:       tex(uwmjuobf.vf) = %{tl_version}, tex(uwmjuoc0.vf) = %{tl_version}
Provides:       tex(uwmjuoc1.vf) = %{tl_version}, tex(uwmjuoc2.vf) = %{tl_version}
Provides:       tex(uwmjuoc3.vf) = %{tl_version}, tex(uwmjuoc4.vf) = %{tl_version}
Provides:       tex(uwmjuoc5.vf) = %{tl_version}, tex(uwmjuoc6.vf) = %{tl_version}
Provides:       tex(uwmjuoc7.vf) = %{tl_version}, tex(uwmjuoc8.vf) = %{tl_version}
Provides:       tex(uwmjuoc9.vf) = %{tl_version}, tex(uwmjuoca.vf) = %{tl_version}
Provides:       tex(uwmjuocb.vf) = %{tl_version}, tex(uwmjuocc.vf) = %{tl_version}
Provides:       tex(uwmjuocd.vf) = %{tl_version}, tex(uwmjuoce.vf) = %{tl_version}
Provides:       tex(uwmjuocf.vf) = %{tl_version}, tex(uwmjuod0.vf) = %{tl_version}
Provides:       tex(uwmjuod1.vf) = %{tl_version}, tex(uwmjuod2.vf) = %{tl_version}
Provides:       tex(uwmjuod3.vf) = %{tl_version}, tex(uwmjuod4.vf) = %{tl_version}
Provides:       tex(uwmjuod5.vf) = %{tl_version}, tex(uwmjuod6.vf) = %{tl_version}
Provides:       tex(uwmjuod7.vf) = %{tl_version}, tex(uwmjuof9.vf) = %{tl_version}
Provides:       tex(uwmjuofa.vf) = %{tl_version}, tex(uwmjuoff.vf) = %{tl_version}
Provides:       tex(uwmjx00.vf) = %{tl_version}, tex(uwmjx01.vf) = %{tl_version}
Provides:       tex(uwmjx02.vf) = %{tl_version}, tex(uwmjx03.vf) = %{tl_version}
Provides:       tex(uwmjx04.vf) = %{tl_version}, tex(uwmjx20.vf) = %{tl_version}
Provides:       tex(uwmjx21.vf) = %{tl_version}, tex(uwmjx22.vf) = %{tl_version}
Provides:       tex(uwmjx23.vf) = %{tl_version}, tex(uwmjx24.vf) = %{tl_version}
Provides:       tex(uwmjx25.vf) = %{tl_version}, tex(uwmjx26.vf) = %{tl_version}
Provides:       tex(uwmjx30.vf) = %{tl_version}, tex(uwmjx31.vf) = %{tl_version}
Provides:       tex(uwmjx32.vf) = %{tl_version}, tex(uwmjx33.vf) = %{tl_version}
Provides:       tex(uwmjx4e.vf) = %{tl_version}, tex(uwmjx4f.vf) = %{tl_version}
Provides:       tex(uwmjx50.vf) = %{tl_version}, tex(uwmjx51.vf) = %{tl_version}
Provides:       tex(uwmjx52.vf) = %{tl_version}, tex(uwmjx53.vf) = %{tl_version}
Provides:       tex(uwmjx54.vf) = %{tl_version}, tex(uwmjx55.vf) = %{tl_version}
Provides:       tex(uwmjx56.vf) = %{tl_version}, tex(uwmjx57.vf) = %{tl_version}
Provides:       tex(uwmjx58.vf) = %{tl_version}, tex(uwmjx59.vf) = %{tl_version}
Provides:       tex(uwmjx5a.vf) = %{tl_version}, tex(uwmjx5b.vf) = %{tl_version}
Provides:       tex(uwmjx5c.vf) = %{tl_version}, tex(uwmjx5d.vf) = %{tl_version}
Provides:       tex(uwmjx5e.vf) = %{tl_version}, tex(uwmjx5f.vf) = %{tl_version}
Provides:       tex(uwmjx60.vf) = %{tl_version}, tex(uwmjx61.vf) = %{tl_version}
Provides:       tex(uwmjx62.vf) = %{tl_version}, tex(uwmjx63.vf) = %{tl_version}
Provides:       tex(uwmjx64.vf) = %{tl_version}, tex(uwmjx65.vf) = %{tl_version}
Provides:       tex(uwmjx66.vf) = %{tl_version}, tex(uwmjx67.vf) = %{tl_version}
Provides:       tex(uwmjx68.vf) = %{tl_version}, tex(uwmjx69.vf) = %{tl_version}
Provides:       tex(uwmjx6a.vf) = %{tl_version}, tex(uwmjx6b.vf) = %{tl_version}
Provides:       tex(uwmjx6c.vf) = %{tl_version}, tex(uwmjx6d.vf) = %{tl_version}
Provides:       tex(uwmjx6e.vf) = %{tl_version}, tex(uwmjx6f.vf) = %{tl_version}
Provides:       tex(uwmjx70.vf) = %{tl_version}, tex(uwmjx71.vf) = %{tl_version}
Provides:       tex(uwmjx72.vf) = %{tl_version}, tex(uwmjx73.vf) = %{tl_version}
Provides:       tex(uwmjx74.vf) = %{tl_version}, tex(uwmjx75.vf) = %{tl_version}
Provides:       tex(uwmjx76.vf) = %{tl_version}, tex(uwmjx77.vf) = %{tl_version}
Provides:       tex(uwmjx78.vf) = %{tl_version}, tex(uwmjx79.vf) = %{tl_version}
Provides:       tex(uwmjx7a.vf) = %{tl_version}, tex(uwmjx7b.vf) = %{tl_version}
Provides:       tex(uwmjx7c.vf) = %{tl_version}, tex(uwmjx7d.vf) = %{tl_version}
Provides:       tex(uwmjx7e.vf) = %{tl_version}, tex(uwmjx7f.vf) = %{tl_version}
Provides:       tex(uwmjx80.vf) = %{tl_version}, tex(uwmjx81.vf) = %{tl_version}
Provides:       tex(uwmjx82.vf) = %{tl_version}, tex(uwmjx83.vf) = %{tl_version}
Provides:       tex(uwmjx84.vf) = %{tl_version}, tex(uwmjx85.vf) = %{tl_version}
Provides:       tex(uwmjx86.vf) = %{tl_version}, tex(uwmjx87.vf) = %{tl_version}
Provides:       tex(uwmjx88.vf) = %{tl_version}, tex(uwmjx89.vf) = %{tl_version}
Provides:       tex(uwmjx8a.vf) = %{tl_version}, tex(uwmjx8b.vf) = %{tl_version}
Provides:       tex(uwmjx8c.vf) = %{tl_version}, tex(uwmjx8d.vf) = %{tl_version}
Provides:       tex(uwmjx8e.vf) = %{tl_version}, tex(uwmjx8f.vf) = %{tl_version}
Provides:       tex(uwmjx90.vf) = %{tl_version}, tex(uwmjx91.vf) = %{tl_version}
Provides:       tex(uwmjx92.vf) = %{tl_version}, tex(uwmjx93.vf) = %{tl_version}
Provides:       tex(uwmjx94.vf) = %{tl_version}, tex(uwmjx95.vf) = %{tl_version}
Provides:       tex(uwmjx96.vf) = %{tl_version}, tex(uwmjx97.vf) = %{tl_version}
Provides:       tex(uwmjx98.vf) = %{tl_version}, tex(uwmjx99.vf) = %{tl_version}
Provides:       tex(uwmjx9a.vf) = %{tl_version}, tex(uwmjx9b.vf) = %{tl_version}
Provides:       tex(uwmjx9c.vf) = %{tl_version}, tex(uwmjx9d.vf) = %{tl_version}
Provides:       tex(uwmjx9e.vf) = %{tl_version}, tex(uwmjx9f.vf) = %{tl_version}
Provides:       tex(uwmjxac.vf) = %{tl_version}, tex(uwmjxad.vf) = %{tl_version}
Provides:       tex(uwmjxae.vf) = %{tl_version}, tex(uwmjxaf.vf) = %{tl_version}
Provides:       tex(uwmjxb0.vf) = %{tl_version}, tex(uwmjxb1.vf) = %{tl_version}
Provides:       tex(uwmjxb2.vf) = %{tl_version}, tex(uwmjxb3.vf) = %{tl_version}
Provides:       tex(uwmjxb4.vf) = %{tl_version}, tex(uwmjxb5.vf) = %{tl_version}
Provides:       tex(uwmjxb6.vf) = %{tl_version}, tex(uwmjxb7.vf) = %{tl_version}
Provides:       tex(uwmjxb8.vf) = %{tl_version}, tex(uwmjxb9.vf) = %{tl_version}
Provides:       tex(uwmjxba.vf) = %{tl_version}, tex(uwmjxbb.vf) = %{tl_version}
Provides:       tex(uwmjxbc.vf) = %{tl_version}, tex(uwmjxbd.vf) = %{tl_version}
Provides:       tex(uwmjxbe.vf) = %{tl_version}, tex(uwmjxbf.vf) = %{tl_version}
Provides:       tex(uwmjxc0.vf) = %{tl_version}, tex(uwmjxc1.vf) = %{tl_version}
Provides:       tex(uwmjxc2.vf) = %{tl_version}, tex(uwmjxc3.vf) = %{tl_version}
Provides:       tex(uwmjxc4.vf) = %{tl_version}, tex(uwmjxc5.vf) = %{tl_version}
Provides:       tex(uwmjxc6.vf) = %{tl_version}, tex(uwmjxc7.vf) = %{tl_version}
Provides:       tex(uwmjxc8.vf) = %{tl_version}, tex(uwmjxc9.vf) = %{tl_version}
Provides:       tex(uwmjxca.vf) = %{tl_version}, tex(uwmjxcb.vf) = %{tl_version}
Provides:       tex(uwmjxcc.vf) = %{tl_version}, tex(uwmjxcd.vf) = %{tl_version}
Provides:       tex(uwmjxce.vf) = %{tl_version}, tex(uwmjxcf.vf) = %{tl_version}
Provides:       tex(uwmjxd0.vf) = %{tl_version}, tex(uwmjxd1.vf) = %{tl_version}
Provides:       tex(uwmjxd2.vf) = %{tl_version}, tex(uwmjxd3.vf) = %{tl_version}
Provides:       tex(uwmjxd4.vf) = %{tl_version}, tex(uwmjxd5.vf) = %{tl_version}
Provides:       tex(uwmjxd6.vf) = %{tl_version}, tex(uwmjxd7.vf) = %{tl_version}
Provides:       tex(uwmjxf9.vf) = %{tl_version}, tex(uwmjxfa.vf) = %{tl_version}
Provides:       tex(uwmjxff.vf) = %{tl_version}, tex(uwmjxo00.vf) = %{tl_version}
Provides:       tex(uwmjxo01.vf) = %{tl_version}, tex(uwmjxo02.vf) = %{tl_version}
Provides:       tex(uwmjxo03.vf) = %{tl_version}, tex(uwmjxo04.vf) = %{tl_version}
Provides:       tex(uwmjxo20.vf) = %{tl_version}, tex(uwmjxo21.vf) = %{tl_version}
Provides:       tex(uwmjxo22.vf) = %{tl_version}, tex(uwmjxo23.vf) = %{tl_version}
Provides:       tex(uwmjxo24.vf) = %{tl_version}, tex(uwmjxo25.vf) = %{tl_version}
Provides:       tex(uwmjxo26.vf) = %{tl_version}, tex(uwmjxo30.vf) = %{tl_version}
Provides:       tex(uwmjxo31.vf) = %{tl_version}, tex(uwmjxo32.vf) = %{tl_version}
Provides:       tex(uwmjxo33.vf) = %{tl_version}, tex(uwmjxo4e.vf) = %{tl_version}
Provides:       tex(uwmjxo4f.vf) = %{tl_version}, tex(uwmjxo50.vf) = %{tl_version}
Provides:       tex(uwmjxo51.vf) = %{tl_version}, tex(uwmjxo52.vf) = %{tl_version}
Provides:       tex(uwmjxo53.vf) = %{tl_version}, tex(uwmjxo54.vf) = %{tl_version}
Provides:       tex(uwmjxo55.vf) = %{tl_version}, tex(uwmjxo56.vf) = %{tl_version}
Provides:       tex(uwmjxo57.vf) = %{tl_version}, tex(uwmjxo58.vf) = %{tl_version}
Provides:       tex(uwmjxo59.vf) = %{tl_version}, tex(uwmjxo5a.vf) = %{tl_version}
Provides:       tex(uwmjxo5b.vf) = %{tl_version}, tex(uwmjxo5c.vf) = %{tl_version}
Provides:       tex(uwmjxo5d.vf) = %{tl_version}, tex(uwmjxo5e.vf) = %{tl_version}
Provides:       tex(uwmjxo5f.vf) = %{tl_version}, tex(uwmjxo60.vf) = %{tl_version}
Provides:       tex(uwmjxo61.vf) = %{tl_version}, tex(uwmjxo62.vf) = %{tl_version}
Provides:       tex(uwmjxo63.vf) = %{tl_version}, tex(uwmjxo64.vf) = %{tl_version}
Provides:       tex(uwmjxo65.vf) = %{tl_version}, tex(uwmjxo66.vf) = %{tl_version}
Provides:       tex(uwmjxo67.vf) = %{tl_version}, tex(uwmjxo68.vf) = %{tl_version}
Provides:       tex(uwmjxo69.vf) = %{tl_version}, tex(uwmjxo6a.vf) = %{tl_version}
Provides:       tex(uwmjxo6b.vf) = %{tl_version}, tex(uwmjxo6c.vf) = %{tl_version}
Provides:       tex(uwmjxo6d.vf) = %{tl_version}, tex(uwmjxo6e.vf) = %{tl_version}
Provides:       tex(uwmjxo6f.vf) = %{tl_version}, tex(uwmjxo70.vf) = %{tl_version}
Provides:       tex(uwmjxo71.vf) = %{tl_version}, tex(uwmjxo72.vf) = %{tl_version}
Provides:       tex(uwmjxo73.vf) = %{tl_version}, tex(uwmjxo74.vf) = %{tl_version}
Provides:       tex(uwmjxo75.vf) = %{tl_version}, tex(uwmjxo76.vf) = %{tl_version}
Provides:       tex(uwmjxo77.vf) = %{tl_version}, tex(uwmjxo78.vf) = %{tl_version}
Provides:       tex(uwmjxo79.vf) = %{tl_version}, tex(uwmjxo7a.vf) = %{tl_version}
Provides:       tex(uwmjxo7b.vf) = %{tl_version}, tex(uwmjxo7c.vf) = %{tl_version}
Provides:       tex(uwmjxo7d.vf) = %{tl_version}, tex(uwmjxo7e.vf) = %{tl_version}
Provides:       tex(uwmjxo7f.vf) = %{tl_version}, tex(uwmjxo80.vf) = %{tl_version}
Provides:       tex(uwmjxo81.vf) = %{tl_version}, tex(uwmjxo82.vf) = %{tl_version}
Provides:       tex(uwmjxo83.vf) = %{tl_version}, tex(uwmjxo84.vf) = %{tl_version}
Provides:       tex(uwmjxo85.vf) = %{tl_version}, tex(uwmjxo86.vf) = %{tl_version}
Provides:       tex(uwmjxo87.vf) = %{tl_version}, tex(uwmjxo88.vf) = %{tl_version}
Provides:       tex(uwmjxo89.vf) = %{tl_version}, tex(uwmjxo8a.vf) = %{tl_version}
Provides:       tex(uwmjxo8b.vf) = %{tl_version}, tex(uwmjxo8c.vf) = %{tl_version}
Provides:       tex(uwmjxo8d.vf) = %{tl_version}, tex(uwmjxo8e.vf) = %{tl_version}
Provides:       tex(uwmjxo8f.vf) = %{tl_version}, tex(uwmjxo90.vf) = %{tl_version}
Provides:       tex(uwmjxo91.vf) = %{tl_version}, tex(uwmjxo92.vf) = %{tl_version}
Provides:       tex(uwmjxo93.vf) = %{tl_version}, tex(uwmjxo94.vf) = %{tl_version}
Provides:       tex(uwmjxo95.vf) = %{tl_version}, tex(uwmjxo96.vf) = %{tl_version}
Provides:       tex(uwmjxo97.vf) = %{tl_version}, tex(uwmjxo98.vf) = %{tl_version}
Provides:       tex(uwmjxo99.vf) = %{tl_version}, tex(uwmjxo9a.vf) = %{tl_version}
Provides:       tex(uwmjxo9b.vf) = %{tl_version}, tex(uwmjxo9c.vf) = %{tl_version}
Provides:       tex(uwmjxo9d.vf) = %{tl_version}, tex(uwmjxo9e.vf) = %{tl_version}
Provides:       tex(uwmjxo9f.vf) = %{tl_version}, tex(uwmjxoac.vf) = %{tl_version}
Provides:       tex(uwmjxoad.vf) = %{tl_version}, tex(uwmjxoae.vf) = %{tl_version}
Provides:       tex(uwmjxoaf.vf) = %{tl_version}, tex(uwmjxob0.vf) = %{tl_version}
Provides:       tex(uwmjxob1.vf) = %{tl_version}, tex(uwmjxob2.vf) = %{tl_version}
Provides:       tex(uwmjxob3.vf) = %{tl_version}, tex(uwmjxob4.vf) = %{tl_version}
Provides:       tex(uwmjxob5.vf) = %{tl_version}, tex(uwmjxob6.vf) = %{tl_version}
Provides:       tex(uwmjxob7.vf) = %{tl_version}, tex(uwmjxob8.vf) = %{tl_version}
Provides:       tex(uwmjxob9.vf) = %{tl_version}, tex(uwmjxoba.vf) = %{tl_version}
Provides:       tex(uwmjxobb.vf) = %{tl_version}, tex(uwmjxobc.vf) = %{tl_version}
Provides:       tex(uwmjxobd.vf) = %{tl_version}, tex(uwmjxobe.vf) = %{tl_version}
Provides:       tex(uwmjxobf.vf) = %{tl_version}, tex(uwmjxoc0.vf) = %{tl_version}
Provides:       tex(uwmjxoc1.vf) = %{tl_version}, tex(uwmjxoc2.vf) = %{tl_version}
Provides:       tex(uwmjxoc3.vf) = %{tl_version}, tex(uwmjxoc4.vf) = %{tl_version}
Provides:       tex(uwmjxoc5.vf) = %{tl_version}, tex(uwmjxoc6.vf) = %{tl_version}
Provides:       tex(uwmjxoc7.vf) = %{tl_version}, tex(uwmjxoc8.vf) = %{tl_version}
Provides:       tex(uwmjxoc9.vf) = %{tl_version}, tex(uwmjxoca.vf) = %{tl_version}
Provides:       tex(uwmjxocb.vf) = %{tl_version}, tex(uwmjxocc.vf) = %{tl_version}
Provides:       tex(uwmjxocd.vf) = %{tl_version}, tex(uwmjxoce.vf) = %{tl_version}
Provides:       tex(uwmjxocf.vf) = %{tl_version}, tex(uwmjxod0.vf) = %{tl_version}
Provides:       tex(uwmjxod1.vf) = %{tl_version}, tex(uwmjxod2.vf) = %{tl_version}
Provides:       tex(uwmjxod3.vf) = %{tl_version}, tex(uwmjxod4.vf) = %{tl_version}
Provides:       tex(uwmjxod5.vf) = %{tl_version}, tex(uwmjxod6.vf) = %{tl_version}
Provides:       tex(uwmjxod7.vf) = %{tl_version}, tex(uwmjxof9.vf) = %{tl_version}
Provides:       tex(uwmjxofa.vf) = %{tl_version}, tex(uwmjxoff.vf) = %{tl_version}
Provides:       tex(wmj0.vf) = %{tl_version}, tex(wmj04.vf) = %{tl_version}
Provides:       tex(wmj05.vf) = %{tl_version}, tex(wmj06.vf) = %{tl_version}
Provides:       tex(wmj07.vf) = %{tl_version}, tex(wmj1.vf) = %{tl_version}
Provides:       tex(wmj10.vf) = %{tl_version}, tex(wmj11.vf) = %{tl_version}
Provides:       tex(wmj12.vf) = %{tl_version}, tex(wmj13.vf) = %{tl_version}
Provides:       tex(wmj14.vf) = %{tl_version}, tex(wmj15.vf) = %{tl_version}
Provides:       tex(wmj16.vf) = %{tl_version}, tex(wmj17.vf) = %{tl_version}
Provides:       tex(wmj18.vf) = %{tl_version}, tex(wmj19.vf) = %{tl_version}
Provides:       tex(wmj2.vf) = %{tl_version}, tex(wmj20.vf) = %{tl_version}
Provides:       tex(wmj21.vf) = %{tl_version}, tex(wmj22.vf) = %{tl_version}
Provides:       tex(wmj23.vf) = %{tl_version}, tex(wmj24.vf) = %{tl_version}
Provides:       tex(wmj25.vf) = %{tl_version}, tex(wmj26.vf) = %{tl_version}
Provides:       tex(wmj27.vf) = %{tl_version}, tex(wmj28.vf) = %{tl_version}
Provides:       tex(wmj29.vf) = %{tl_version}, tex(wmj3.vf) = %{tl_version}
Provides:       tex(wmj4.vf) = %{tl_version}, tex(wmj5.vf) = %{tl_version}
Provides:       tex(wmj6.vf) = %{tl_version}, tex(wmj7.vf) = %{tl_version}
Provides:       tex(wmj8.vf) = %{tl_version}, tex(wmj9.vf) = %{tl_version}
Provides:       tex(wmjc0.vf) = %{tl_version}, tex(wmjc04.vf) = %{tl_version}
Provides:       tex(wmjc05.vf) = %{tl_version}, tex(wmjc06.vf) = %{tl_version}
Provides:       tex(wmjc07.vf) = %{tl_version}, tex(wmjc1.vf) = %{tl_version}
Provides:       tex(wmjc10.vf) = %{tl_version}, tex(wmjc11.vf) = %{tl_version}
Provides:       tex(wmjc12.vf) = %{tl_version}, tex(wmjc13.vf) = %{tl_version}
Provides:       tex(wmjc14.vf) = %{tl_version}, tex(wmjc15.vf) = %{tl_version}
Provides:       tex(wmjc16.vf) = %{tl_version}, tex(wmjc17.vf) = %{tl_version}
Provides:       tex(wmjc18.vf) = %{tl_version}, tex(wmjc19.vf) = %{tl_version}
Provides:       tex(wmjc2.vf) = %{tl_version}, tex(wmjc20.vf) = %{tl_version}
Provides:       tex(wmjc21.vf) = %{tl_version}, tex(wmjc22.vf) = %{tl_version}
Provides:       tex(wmjc23.vf) = %{tl_version}, tex(wmjc24.vf) = %{tl_version}
Provides:       tex(wmjc25.vf) = %{tl_version}, tex(wmjc26.vf) = %{tl_version}
Provides:       tex(wmjc27.vf) = %{tl_version}, tex(wmjc28.vf) = %{tl_version}
Provides:       tex(wmjc29.vf) = %{tl_version}, tex(wmjc3.vf) = %{tl_version}
Provides:       tex(wmjc4.vf) = %{tl_version}, tex(wmjc5.vf) = %{tl_version}
Provides:       tex(wmjc6.vf) = %{tl_version}, tex(wmjc7.vf) = %{tl_version}
Provides:       tex(wmjc8.vf) = %{tl_version}, tex(wmjc9.vf) = %{tl_version}
Provides:       tex(wmjco0.vf) = %{tl_version}, tex(wmjco04.vf) = %{tl_version}
Provides:       tex(wmjco05.vf) = %{tl_version}, tex(wmjco06.vf) = %{tl_version}
Provides:       tex(wmjco07.vf) = %{tl_version}, tex(wmjco1.vf) = %{tl_version}
Provides:       tex(wmjco10.vf) = %{tl_version}, tex(wmjco11.vf) = %{tl_version}
Provides:       tex(wmjco12.vf) = %{tl_version}, tex(wmjco13.vf) = %{tl_version}
Provides:       tex(wmjco14.vf) = %{tl_version}, tex(wmjco15.vf) = %{tl_version}
Provides:       tex(wmjco16.vf) = %{tl_version}, tex(wmjco17.vf) = %{tl_version}
Provides:       tex(wmjco18.vf) = %{tl_version}, tex(wmjco19.vf) = %{tl_version}
Provides:       tex(wmjco2.vf) = %{tl_version}, tex(wmjco20.vf) = %{tl_version}
Provides:       tex(wmjco21.vf) = %{tl_version}, tex(wmjco22.vf) = %{tl_version}
Provides:       tex(wmjco23.vf) = %{tl_version}, tex(wmjco24.vf) = %{tl_version}
Provides:       tex(wmjco25.vf) = %{tl_version}, tex(wmjco26.vf) = %{tl_version}
Provides:       tex(wmjco27.vf) = %{tl_version}, tex(wmjco28.vf) = %{tl_version}
Provides:       tex(wmjco29.vf) = %{tl_version}, tex(wmjco3.vf) = %{tl_version}
Provides:       tex(wmjco4.vf) = %{tl_version}, tex(wmjco5.vf) = %{tl_version}
Provides:       tex(wmjco6.vf) = %{tl_version}, tex(wmjco7.vf) = %{tl_version}
Provides:       tex(wmjco8.vf) = %{tl_version}, tex(wmjco9.vf) = %{tl_version}
Provides:       tex(wmjo0.vf) = %{tl_version}, tex(wmjo04.vf) = %{tl_version}
Provides:       tex(wmjo05.vf) = %{tl_version}, tex(wmjo06.vf) = %{tl_version}
Provides:       tex(wmjo07.vf) = %{tl_version}, tex(wmjo1.vf) = %{tl_version}
Provides:       tex(wmjo10.vf) = %{tl_version}, tex(wmjo11.vf) = %{tl_version}
Provides:       tex(wmjo12.vf) = %{tl_version}, tex(wmjo13.vf) = %{tl_version}
Provides:       tex(wmjo14.vf) = %{tl_version}, tex(wmjo15.vf) = %{tl_version}
Provides:       tex(wmjo16.vf) = %{tl_version}, tex(wmjo17.vf) = %{tl_version}
Provides:       tex(wmjo18.vf) = %{tl_version}, tex(wmjo19.vf) = %{tl_version}
Provides:       tex(wmjo2.vf) = %{tl_version}, tex(wmjo20.vf) = %{tl_version}
Provides:       tex(wmjo21.vf) = %{tl_version}, tex(wmjo22.vf) = %{tl_version}
Provides:       tex(wmjo23.vf) = %{tl_version}, tex(wmjo24.vf) = %{tl_version}
Provides:       tex(wmjo25.vf) = %{tl_version}, tex(wmjo26.vf) = %{tl_version}
Provides:       tex(wmjo27.vf) = %{tl_version}, tex(wmjo28.vf) = %{tl_version}
Provides:       tex(wmjo29.vf) = %{tl_version}, tex(wmjo3.vf) = %{tl_version}
Provides:       tex(wmjo4.vf) = %{tl_version}, tex(wmjo5.vf) = %{tl_version}
Provides:       tex(wmjo6.vf) = %{tl_version}, tex(wmjo7.vf) = %{tl_version}
Provides:       tex(wmjo8.vf) = %{tl_version}, tex(wmjo9.vf) = %{tl_version}
Provides:       tex(wmju0.vf) = %{tl_version}, tex(wmju04.vf) = %{tl_version}
Provides:       tex(wmju05.vf) = %{tl_version}, tex(wmju06.vf) = %{tl_version}
Provides:       tex(wmju07.vf) = %{tl_version}, tex(wmju1.vf) = %{tl_version}
Provides:       tex(wmju10.vf) = %{tl_version}, tex(wmju11.vf) = %{tl_version}
Provides:       tex(wmju12.vf) = %{tl_version}, tex(wmju13.vf) = %{tl_version}
Provides:       tex(wmju14.vf) = %{tl_version}, tex(wmju15.vf) = %{tl_version}
Provides:       tex(wmju16.vf) = %{tl_version}, tex(wmju17.vf) = %{tl_version}
Provides:       tex(wmju18.vf) = %{tl_version}, tex(wmju19.vf) = %{tl_version}
Provides:       tex(wmju2.vf) = %{tl_version}, tex(wmju20.vf) = %{tl_version}
Provides:       tex(wmju21.vf) = %{tl_version}, tex(wmju22.vf) = %{tl_version}
Provides:       tex(wmju23.vf) = %{tl_version}, tex(wmju24.vf) = %{tl_version}
Provides:       tex(wmju25.vf) = %{tl_version}, tex(wmju26.vf) = %{tl_version}
Provides:       tex(wmju27.vf) = %{tl_version}, tex(wmju28.vf) = %{tl_version}
Provides:       tex(wmju29.vf) = %{tl_version}, tex(wmju3.vf) = %{tl_version}
Provides:       tex(wmju4.vf) = %{tl_version}, tex(wmju5.vf) = %{tl_version}
Provides:       tex(wmju6.vf) = %{tl_version}, tex(wmju7.vf) = %{tl_version}
Provides:       tex(wmju8.vf) = %{tl_version}, tex(wmju9.vf) = %{tl_version}
Provides:       tex(wmjuo0.vf) = %{tl_version}, tex(wmjuo04.vf) = %{tl_version}
Provides:       tex(wmjuo05.vf) = %{tl_version}, tex(wmjuo06.vf) = %{tl_version}
Provides:       tex(wmjuo07.vf) = %{tl_version}, tex(wmjuo1.vf) = %{tl_version}
Provides:       tex(wmjuo10.vf) = %{tl_version}, tex(wmjuo11.vf) = %{tl_version}
Provides:       tex(wmjuo12.vf) = %{tl_version}, tex(wmjuo13.vf) = %{tl_version}
Provides:       tex(wmjuo14.vf) = %{tl_version}, tex(wmjuo15.vf) = %{tl_version}
Provides:       tex(wmjuo16.vf) = %{tl_version}, tex(wmjuo17.vf) = %{tl_version}
Provides:       tex(wmjuo18.vf) = %{tl_version}, tex(wmjuo19.vf) = %{tl_version}
Provides:       tex(wmjuo2.vf) = %{tl_version}, tex(wmjuo20.vf) = %{tl_version}
Provides:       tex(wmjuo21.vf) = %{tl_version}, tex(wmjuo22.vf) = %{tl_version}
Provides:       tex(wmjuo23.vf) = %{tl_version}, tex(wmjuo24.vf) = %{tl_version}
Provides:       tex(wmjuo25.vf) = %{tl_version}, tex(wmjuo26.vf) = %{tl_version}
Provides:       tex(wmjuo27.vf) = %{tl_version}, tex(wmjuo28.vf) = %{tl_version}
Provides:       tex(wmjuo29.vf) = %{tl_version}, tex(wmjuo3.vf) = %{tl_version}
Provides:       tex(wmjuo4.vf) = %{tl_version}, tex(wmjuo5.vf) = %{tl_version}
Provides:       tex(wmjuo6.vf) = %{tl_version}, tex(wmjuo7.vf) = %{tl_version}
Provides:       tex(wmjuo8.vf) = %{tl_version}, tex(wmjuo9.vf) = %{tl_version}
Provides:       tex(wmjx0.vf) = %{tl_version}, tex(wmjx04.vf) = %{tl_version}
Provides:       tex(wmjx05.vf) = %{tl_version}, tex(wmjx06.vf) = %{tl_version}
Provides:       tex(wmjx07.vf) = %{tl_version}, tex(wmjx1.vf) = %{tl_version}
Provides:       tex(wmjx10.vf) = %{tl_version}, tex(wmjx11.vf) = %{tl_version}
Provides:       tex(wmjx12.vf) = %{tl_version}, tex(wmjx13.vf) = %{tl_version}
Provides:       tex(wmjx14.vf) = %{tl_version}, tex(wmjx15.vf) = %{tl_version}
Provides:       tex(wmjx16.vf) = %{tl_version}, tex(wmjx17.vf) = %{tl_version}
Provides:       tex(wmjx18.vf) = %{tl_version}, tex(wmjx19.vf) = %{tl_version}
Provides:       tex(wmjx2.vf) = %{tl_version}, tex(wmjx20.vf) = %{tl_version}
Provides:       tex(wmjx21.vf) = %{tl_version}, tex(wmjx22.vf) = %{tl_version}
Provides:       tex(wmjx23.vf) = %{tl_version}, tex(wmjx24.vf) = %{tl_version}
Provides:       tex(wmjx25.vf) = %{tl_version}, tex(wmjx26.vf) = %{tl_version}
Provides:       tex(wmjx27.vf) = %{tl_version}, tex(wmjx28.vf) = %{tl_version}
Provides:       tex(wmjx29.vf) = %{tl_version}, tex(wmjx3.vf) = %{tl_version}
Provides:       tex(wmjx4.vf) = %{tl_version}, tex(wmjx5.vf) = %{tl_version}
Provides:       tex(wmjx6.vf) = %{tl_version}, tex(wmjx7.vf) = %{tl_version}
Provides:       tex(wmjx8.vf) = %{tl_version}, tex(wmjx9.vf) = %{tl_version}
Provides:       tex(wmjxo0.vf) = %{tl_version}, tex(wmjxo04.vf) = %{tl_version}
Provides:       tex(wmjxo05.vf) = %{tl_version}, tex(wmjxo06.vf) = %{tl_version}
Provides:       tex(wmjxo07.vf) = %{tl_version}, tex(wmjxo1.vf) = %{tl_version}
Provides:       tex(wmjxo10.vf) = %{tl_version}, tex(wmjxo11.vf) = %{tl_version}
Provides:       tex(wmjxo12.vf) = %{tl_version}, tex(wmjxo13.vf) = %{tl_version}
Provides:       tex(wmjxo14.vf) = %{tl_version}, tex(wmjxo15.vf) = %{tl_version}
Provides:       tex(wmjxo16.vf) = %{tl_version}, tex(wmjxo17.vf) = %{tl_version}
Provides:       tex(wmjxo18.vf) = %{tl_version}, tex(wmjxo19.vf) = %{tl_version}
Provides:       tex(wmjxo2.vf) = %{tl_version}, tex(wmjxo20.vf) = %{tl_version}
Provides:       tex(wmjxo21.vf) = %{tl_version}, tex(wmjxo22.vf) = %{tl_version}
Provides:       tex(wmjxo23.vf) = %{tl_version}, tex(wmjxo24.vf) = %{tl_version}
Provides:       tex(wmjxo25.vf) = %{tl_version}, tex(wmjxo26.vf) = %{tl_version}
Provides:       tex(wmjxo27.vf) = %{tl_version}, tex(wmjxo28.vf) = %{tl_version}
Provides:       tex(wmjxo29.vf) = %{tl_version}, tex(wmjxo3.vf) = %{tl_version}
Provides:       tex(wmjxo4.vf) = %{tl_version}, tex(wmjxo5.vf) = %{tl_version}
Provides:       tex(wmjxo6.vf) = %{tl_version}, tex(wmjxo7.vf) = %{tl_version}
Provides:       tex(wmjxo8.vf) = %{tl_version}, tex(wmjxo9.vf) = %{tl_version}

%description -n texlive-uhc
Support for Korean documents written in Korean standard KSC
codes for LaTeX2e.

%package -n texlive-uhc-doc
Summary:        Documentation for uhc
Version:        svn16791.0

Provides:       tex-uhc-doc
AutoReqProv:    No

%description -n texlive-uhc-doc
Documentation for uhc

%package -n texlive-ukrhyph
Provides:       tex-ukrhyph = %{tl_version}
License:        LPPL
Summary:        Hyphenation Patterns for Ukrainian
Version:        svn21081.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(catlcy.tex) = %{tl_version}, tex(lcy2koi.tex) = %{tl_version}
Provides:       tex(lcy2lcy.tex) = %{tl_version}, tex(lcy2ot2.tex) = %{tl_version}
Provides:       tex(lcy2t2a.tex) = %{tl_version}, tex(lcy2ucy.tex) = %{tl_version}
Provides:       tex(rules60.tex) = %{tl_version}, tex(rules90.tex) = %{tl_version}
Provides:       tex(rules_ph.tex) = %{tl_version}, tex(ukrenhyp.tex) = %{tl_version}
Provides:       tex(ukrhypfa.tex) = %{tl_version}, tex(ukrhyph.tex) = %{tl_version}
Provides:       tex(ukrhypmp.tex) = %{tl_version}, tex(ukrhypmt.tex) = %{tl_version}
Provides:       tex(ukrhypsm.tex) = %{tl_version}, tex(ukrhypst.tex) = %{tl_version}

%description -n texlive-ukrhyph
A range of patterns, depending on the encoding of the output
font (including the standard T2A, so one can use the patterns
with free fonts).

%package -n texlive-ukrhyph-doc
Summary:        Documentation for ukrhyph
Version:        svn21081.0

Provides:       tex-ukrhyph-doc
AutoReqProv:    No

%description -n texlive-ukrhyph-doc
Documentation for ukrhyph

%package -n texlive-wadalab
Provides:       tex-wadalab = %{tl_version}
License:        Wadalab
Summary:        Wadalab (Japanese) font packages
Version:        svn42428
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Provides:       tex(dgj.map) = %{tl_version}, tex(dmj.map) = %{tl_version}
Provides:       tex(mc2j.map) = %{tl_version}, tex(mcj.map) = %{tl_version}
Provides:       tex(mr2j.map) = %{tl_version}, tex(mrj.map) = %{tl_version}
Provides:       tex(dgjgreek.tfm) = %{tl_version}, tex(dgjhira.tfm) = %{tl_version}
Provides:       tex(dgjhw.tfm) = %{tl_version}, tex(dgjka.tfm) = %{tl_version}
Provides:       tex(dgjkata.tfm) = %{tl_version}, tex(dgjkb.tfm) = %{tl_version}
Provides:       tex(dgjkc.tfm) = %{tl_version}, tex(dgjkd.tfm) = %{tl_version}
Provides:       tex(dgjke.tfm) = %{tl_version}, tex(dgjkeisen.tfm) = %{tl_version}
Provides:       tex(dgjkf.tfm) = %{tl_version}, tex(dgjkg.tfm) = %{tl_version}
Provides:       tex(dgjkh.tfm) = %{tl_version}, tex(dgjki.tfm) = %{tl_version}
Provides:       tex(dgjkj.tfm) = %{tl_version}, tex(dgjkk.tfm) = %{tl_version}
Provides:       tex(dgjkl.tfm) = %{tl_version}, tex(dgjkm.tfm) = %{tl_version}
Provides:       tex(dgjkn.tfm) = %{tl_version}, tex(dgjko.tfm) = %{tl_version}
Provides:       tex(dgjkp.tfm) = %{tl_version}, tex(dgjkq.tfm) = %{tl_version}
Provides:       tex(dgjkr.tfm) = %{tl_version}, tex(dgjks.tfm) = %{tl_version}
Provides:       tex(dgjkt.tfm) = %{tl_version}, tex(dgjku.tfm) = %{tl_version}
Provides:       tex(dgjkv.tfm) = %{tl_version}, tex(dgjkw.tfm) = %{tl_version}
Provides:       tex(dgjkx.tfm) = %{tl_version}, tex(dgjky.tfm) = %{tl_version}
Provides:       tex(dgjkz.tfm) = %{tl_version}, tex(dgjroma.tfm) = %{tl_version}
Provides:       tex(dgjrussian.tfm) = %{tl_version}, tex(dgjsy.tfm) = %{tl_version}
Provides:       tex(dmjgreek.tfm) = %{tl_version}, tex(dmjhira.tfm) = %{tl_version}
Provides:       tex(dmjhw.tfm) = %{tl_version}, tex(dmjka.tfm) = %{tl_version}
Provides:       tex(dmjkata.tfm) = %{tl_version}, tex(dmjkb.tfm) = %{tl_version}
Provides:       tex(dmjkc.tfm) = %{tl_version}, tex(dmjkd.tfm) = %{tl_version}
Provides:       tex(dmjke.tfm) = %{tl_version}, tex(dmjkeisen.tfm) = %{tl_version}
Provides:       tex(dmjkf.tfm) = %{tl_version}, tex(dmjkg.tfm) = %{tl_version}
Provides:       tex(dmjkh.tfm) = %{tl_version}, tex(dmjki.tfm) = %{tl_version}
Provides:       tex(dmjkj.tfm) = %{tl_version}, tex(dmjkk.tfm) = %{tl_version}
Provides:       tex(dmjkl.tfm) = %{tl_version}, tex(dmjkm.tfm) = %{tl_version}
Provides:       tex(dmjkn.tfm) = %{tl_version}, tex(dmjko.tfm) = %{tl_version}
Provides:       tex(dmjkp.tfm) = %{tl_version}, tex(dmjkq.tfm) = %{tl_version}
Provides:       tex(dmjkr.tfm) = %{tl_version}, tex(dmjks.tfm) = %{tl_version}
Provides:       tex(dmjkt.tfm) = %{tl_version}, tex(dmjku.tfm) = %{tl_version}
Provides:       tex(dmjkv.tfm) = %{tl_version}, tex(dmjkw.tfm) = %{tl_version}
Provides:       tex(dmjkx.tfm) = %{tl_version}, tex(dmjky.tfm) = %{tl_version}
Provides:       tex(dmjkz.tfm) = %{tl_version}, tex(dmjroma.tfm) = %{tl_version}
Provides:       tex(dmjrussian.tfm) = %{tl_version}, tex(dmjsy.tfm) = %{tl_version}
Provides:       tex(mc2jka.tfm) = %{tl_version}, tex(mc2jkb.tfm) = %{tl_version}
Provides:       tex(mc2jkc.tfm) = %{tl_version}, tex(mc2jkd.tfm) = %{tl_version}
Provides:       tex(mc2jke.tfm) = %{tl_version}, tex(mc2jkf.tfm) = %{tl_version}
Provides:       tex(mc2jkg.tfm) = %{tl_version}, tex(mc2jkh.tfm) = %{tl_version}
Provides:       tex(mc2jki.tfm) = %{tl_version}, tex(mc2jkj.tfm) = %{tl_version}
Provides:       tex(mc2jkk.tfm) = %{tl_version}, tex(mc2jkl.tfm) = %{tl_version}
Provides:       tex(mc2jkm.tfm) = %{tl_version}, tex(mc2jkn.tfm) = %{tl_version}
Provides:       tex(mc2jko.tfm) = %{tl_version}, tex(mc2jkp.tfm) = %{tl_version}
Provides:       tex(mc2jkq.tfm) = %{tl_version}, tex(mc2jkr.tfm) = %{tl_version}
Provides:       tex(mc2jks.tfm) = %{tl_version}, tex(mc2jkt.tfm) = %{tl_version}
Provides:       tex(mc2jku.tfm) = %{tl_version}, tex(mc2jkv.tfm) = %{tl_version}
Provides:       tex(mc2jkw.tfm) = %{tl_version}, tex(mcjgreek.tfm) = %{tl_version}
Provides:       tex(mcjhira.tfm) = %{tl_version}, tex(mcjhw.tfm) = %{tl_version}
Provides:       tex(mcjka.tfm) = %{tl_version}, tex(mcjkata.tfm) = %{tl_version}
Provides:       tex(mcjkb.tfm) = %{tl_version}, tex(mcjkc.tfm) = %{tl_version}
Provides:       tex(mcjkd.tfm) = %{tl_version}, tex(mcjke.tfm) = %{tl_version}
Provides:       tex(mcjkeisen.tfm) = %{tl_version}, tex(mcjkf.tfm) = %{tl_version}
Provides:       tex(mcjkg.tfm) = %{tl_version}, tex(mcjkh.tfm) = %{tl_version}
Provides:       tex(mcjki.tfm) = %{tl_version}, tex(mcjkj.tfm) = %{tl_version}
Provides:       tex(mcjkk.tfm) = %{tl_version}, tex(mcjkl.tfm) = %{tl_version}
Provides:       tex(mcjkm.tfm) = %{tl_version}, tex(mcjkn.tfm) = %{tl_version}
Provides:       tex(mcjko.tfm) = %{tl_version}, tex(mcjkp.tfm) = %{tl_version}
Provides:       tex(mcjkq.tfm) = %{tl_version}, tex(mcjkr.tfm) = %{tl_version}
Provides:       tex(mcjks.tfm) = %{tl_version}, tex(mcjkt.tfm) = %{tl_version}
Provides:       tex(mcjku.tfm) = %{tl_version}, tex(mcjkv.tfm) = %{tl_version}
Provides:       tex(mcjkw.tfm) = %{tl_version}, tex(mcjkx.tfm) = %{tl_version}
Provides:       tex(mcjky.tfm) = %{tl_version}, tex(mcjkz.tfm) = %{tl_version}
Provides:       tex(mcjroma.tfm) = %{tl_version}, tex(mcjrussian.tfm) = %{tl_version}
Provides:       tex(mcjsy.tfm) = %{tl_version}, tex(mr2jka.tfm) = %{tl_version}
Provides:       tex(mr2jkb.tfm) = %{tl_version}, tex(mr2jkc.tfm) = %{tl_version}
Provides:       tex(mr2jkd.tfm) = %{tl_version}, tex(mr2jke.tfm) = %{tl_version}
Provides:       tex(mr2jkf.tfm) = %{tl_version}, tex(mr2jkg.tfm) = %{tl_version}
Provides:       tex(mr2jkh.tfm) = %{tl_version}, tex(mr2jki.tfm) = %{tl_version}
Provides:       tex(mr2jkj.tfm) = %{tl_version}, tex(mr2jkk.tfm) = %{tl_version}
Provides:       tex(mr2jkl.tfm) = %{tl_version}, tex(mr2jkm.tfm) = %{tl_version}
Provides:       tex(mr2jkn.tfm) = %{tl_version}, tex(mr2jko.tfm) = %{tl_version}
Provides:       tex(mr2jkp.tfm) = %{tl_version}, tex(mr2jkq.tfm) = %{tl_version}
Provides:       tex(mr2jkr.tfm) = %{tl_version}, tex(mr2jks.tfm) = %{tl_version}
Provides:       tex(mr2jkt.tfm) = %{tl_version}, tex(mr2jku.tfm) = %{tl_version}
Provides:       tex(mr2jkv.tfm) = %{tl_version}, tex(mr2jkw.tfm) = %{tl_version}
Provides:       tex(mrjgreek.tfm) = %{tl_version}, tex(mrjhira.tfm) = %{tl_version}
Provides:       tex(mrjhw.tfm) = %{tl_version}, tex(mrjka.tfm) = %{tl_version}
Provides:       tex(mrjkata.tfm) = %{tl_version}, tex(mrjkb.tfm) = %{tl_version}
Provides:       tex(mrjkc.tfm) = %{tl_version}, tex(mrjkd.tfm) = %{tl_version}
Provides:       tex(mrjke.tfm) = %{tl_version}, tex(mrjkeisen.tfm) = %{tl_version}
Provides:       tex(mrjkf.tfm) = %{tl_version}, tex(mrjkg.tfm) = %{tl_version}
Provides:       tex(mrjkh.tfm) = %{tl_version}, tex(mrjki.tfm) = %{tl_version}
Provides:       tex(mrjkj.tfm) = %{tl_version}, tex(mrjkk.tfm) = %{tl_version}
Provides:       tex(mrjkl.tfm) = %{tl_version}, tex(mrjkm.tfm) = %{tl_version}
Provides:       tex(mrjkn.tfm) = %{tl_version}, tex(mrjko.tfm) = %{tl_version}
Provides:       tex(mrjkp.tfm) = %{tl_version}, tex(mrjkq.tfm) = %{tl_version}
Provides:       tex(mrjkr.tfm) = %{tl_version}, tex(mrjks.tfm) = %{tl_version}
Provides:       tex(mrjkt.tfm) = %{tl_version}, tex(mrjku.tfm) = %{tl_version}
Provides:       tex(mrjkv.tfm) = %{tl_version}, tex(mrjkw.tfm) = %{tl_version}
Provides:       tex(mrjkx.tfm) = %{tl_version}, tex(mrjky.tfm) = %{tl_version}
Provides:       tex(mrjkz.tfm) = %{tl_version}, tex(mrjroma.tfm) = %{tl_version}
Provides:       tex(mrjrussian.tfm) = %{tl_version}, tex(mrjsy.tfm) = %{tl_version}
Provides:       tex(udgj00.tfm) = %{tl_version}, tex(udgj03.tfm) = %{tl_version}
Provides:       tex(udgj04.tfm) = %{tl_version}, tex(udgj20.tfm) = %{tl_version}
Provides:       tex(udgj21.tfm) = %{tl_version}, tex(udgj22.tfm) = %{tl_version}
Provides:       tex(udgj23.tfm) = %{tl_version}, tex(udgj25.tfm) = %{tl_version}
Provides:       tex(udgj26.tfm) = %{tl_version}, tex(udgj30.tfm) = %{tl_version}
Provides:       tex(udgj4e.tfm) = %{tl_version}, tex(udgj4f.tfm) = %{tl_version}
Provides:       tex(udgj50.tfm) = %{tl_version}, tex(udgj51.tfm) = %{tl_version}
Provides:       tex(udgj52.tfm) = %{tl_version}, tex(udgj53.tfm) = %{tl_version}
Provides:       tex(udgj54.tfm) = %{tl_version}, tex(udgj55.tfm) = %{tl_version}
Provides:       tex(udgj56.tfm) = %{tl_version}, tex(udgj57.tfm) = %{tl_version}
Provides:       tex(udgj58.tfm) = %{tl_version}, tex(udgj59.tfm) = %{tl_version}
Provides:       tex(udgj5a.tfm) = %{tl_version}, tex(udgj5b.tfm) = %{tl_version}
Provides:       tex(udgj5c.tfm) = %{tl_version}, tex(udgj5d.tfm) = %{tl_version}
Provides:       tex(udgj5e.tfm) = %{tl_version}, tex(udgj5f.tfm) = %{tl_version}
Provides:       tex(udgj60.tfm) = %{tl_version}, tex(udgj61.tfm) = %{tl_version}
Provides:       tex(udgj62.tfm) = %{tl_version}, tex(udgj63.tfm) = %{tl_version}
Provides:       tex(udgj64.tfm) = %{tl_version}, tex(udgj65.tfm) = %{tl_version}
Provides:       tex(udgj66.tfm) = %{tl_version}, tex(udgj67.tfm) = %{tl_version}
Provides:       tex(udgj68.tfm) = %{tl_version}, tex(udgj69.tfm) = %{tl_version}
Provides:       tex(udgj6a.tfm) = %{tl_version}, tex(udgj6b.tfm) = %{tl_version}
Provides:       tex(udgj6c.tfm) = %{tl_version}, tex(udgj6d.tfm) = %{tl_version}
Provides:       tex(udgj6e.tfm) = %{tl_version}, tex(udgj6f.tfm) = %{tl_version}
Provides:       tex(udgj70.tfm) = %{tl_version}, tex(udgj71.tfm) = %{tl_version}
Provides:       tex(udgj72.tfm) = %{tl_version}, tex(udgj73.tfm) = %{tl_version}
Provides:       tex(udgj74.tfm) = %{tl_version}, tex(udgj75.tfm) = %{tl_version}
Provides:       tex(udgj76.tfm) = %{tl_version}, tex(udgj77.tfm) = %{tl_version}
Provides:       tex(udgj78.tfm) = %{tl_version}, tex(udgj79.tfm) = %{tl_version}
Provides:       tex(udgj7a.tfm) = %{tl_version}, tex(udgj7b.tfm) = %{tl_version}
Provides:       tex(udgj7c.tfm) = %{tl_version}, tex(udgj7d.tfm) = %{tl_version}
Provides:       tex(udgj7e.tfm) = %{tl_version}, tex(udgj7f.tfm) = %{tl_version}
Provides:       tex(udgj80.tfm) = %{tl_version}, tex(udgj81.tfm) = %{tl_version}
Provides:       tex(udgj82.tfm) = %{tl_version}, tex(udgj83.tfm) = %{tl_version}
Provides:       tex(udgj84.tfm) = %{tl_version}, tex(udgj85.tfm) = %{tl_version}
Provides:       tex(udgj86.tfm) = %{tl_version}, tex(udgj87.tfm) = %{tl_version}
Provides:       tex(udgj88.tfm) = %{tl_version}, tex(udgj89.tfm) = %{tl_version}
Provides:       tex(udgj8a.tfm) = %{tl_version}, tex(udgj8b.tfm) = %{tl_version}
Provides:       tex(udgj8c.tfm) = %{tl_version}, tex(udgj8d.tfm) = %{tl_version}
Provides:       tex(udgj8e.tfm) = %{tl_version}, tex(udgj8f.tfm) = %{tl_version}
Provides:       tex(udgj90.tfm) = %{tl_version}, tex(udgj91.tfm) = %{tl_version}
Provides:       tex(udgj92.tfm) = %{tl_version}, tex(udgj93.tfm) = %{tl_version}
Provides:       tex(udgj94.tfm) = %{tl_version}, tex(udgj95.tfm) = %{tl_version}
Provides:       tex(udgj96.tfm) = %{tl_version}, tex(udgj97.tfm) = %{tl_version}
Provides:       tex(udgj98.tfm) = %{tl_version}, tex(udgj99.tfm) = %{tl_version}
Provides:       tex(udgj9a.tfm) = %{tl_version}, tex(udgj9b.tfm) = %{tl_version}
Provides:       tex(udgj9c.tfm) = %{tl_version}, tex(udgj9d.tfm) = %{tl_version}
Provides:       tex(udgj9e.tfm) = %{tl_version}, tex(udgj9f.tfm) = %{tl_version}
Provides:       tex(udgjff.tfm) = %{tl_version}, tex(udmj00.tfm) = %{tl_version}
Provides:       tex(udmj03.tfm) = %{tl_version}, tex(udmj04.tfm) = %{tl_version}
Provides:       tex(udmj20.tfm) = %{tl_version}, tex(udmj21.tfm) = %{tl_version}
Provides:       tex(udmj22.tfm) = %{tl_version}, tex(udmj23.tfm) = %{tl_version}
Provides:       tex(udmj25.tfm) = %{tl_version}, tex(udmj26.tfm) = %{tl_version}
Provides:       tex(udmj30.tfm) = %{tl_version}, tex(udmj4e.tfm) = %{tl_version}
Provides:       tex(udmj4f.tfm) = %{tl_version}, tex(udmj50.tfm) = %{tl_version}
Provides:       tex(udmj51.tfm) = %{tl_version}, tex(udmj52.tfm) = %{tl_version}
Provides:       tex(udmj53.tfm) = %{tl_version}, tex(udmj54.tfm) = %{tl_version}
Provides:       tex(udmj55.tfm) = %{tl_version}, tex(udmj56.tfm) = %{tl_version}
Provides:       tex(udmj57.tfm) = %{tl_version}, tex(udmj58.tfm) = %{tl_version}
Provides:       tex(udmj59.tfm) = %{tl_version}, tex(udmj5a.tfm) = %{tl_version}
Provides:       tex(udmj5b.tfm) = %{tl_version}, tex(udmj5c.tfm) = %{tl_version}
Provides:       tex(udmj5d.tfm) = %{tl_version}, tex(udmj5e.tfm) = %{tl_version}
Provides:       tex(udmj5f.tfm) = %{tl_version}, tex(udmj60.tfm) = %{tl_version}
Provides:       tex(udmj61.tfm) = %{tl_version}, tex(udmj62.tfm) = %{tl_version}
Provides:       tex(udmj63.tfm) = %{tl_version}, tex(udmj64.tfm) = %{tl_version}
Provides:       tex(udmj65.tfm) = %{tl_version}, tex(udmj66.tfm) = %{tl_version}
Provides:       tex(udmj67.tfm) = %{tl_version}, tex(udmj68.tfm) = %{tl_version}
Provides:       tex(udmj69.tfm) = %{tl_version}, tex(udmj6a.tfm) = %{tl_version}
Provides:       tex(udmj6b.tfm) = %{tl_version}, tex(udmj6c.tfm) = %{tl_version}
Provides:       tex(udmj6d.tfm) = %{tl_version}, tex(udmj6e.tfm) = %{tl_version}
Provides:       tex(udmj6f.tfm) = %{tl_version}, tex(udmj70.tfm) = %{tl_version}
Provides:       tex(udmj71.tfm) = %{tl_version}, tex(udmj72.tfm) = %{tl_version}
Provides:       tex(udmj73.tfm) = %{tl_version}, tex(udmj74.tfm) = %{tl_version}
Provides:       tex(udmj75.tfm) = %{tl_version}, tex(udmj76.tfm) = %{tl_version}
Provides:       tex(udmj77.tfm) = %{tl_version}, tex(udmj78.tfm) = %{tl_version}
Provides:       tex(udmj79.tfm) = %{tl_version}, tex(udmj7a.tfm) = %{tl_version}
Provides:       tex(udmj7b.tfm) = %{tl_version}, tex(udmj7c.tfm) = %{tl_version}
Provides:       tex(udmj7d.tfm) = %{tl_version}, tex(udmj7e.tfm) = %{tl_version}
Provides:       tex(udmj7f.tfm) = %{tl_version}, tex(udmj80.tfm) = %{tl_version}
Provides:       tex(udmj81.tfm) = %{tl_version}, tex(udmj82.tfm) = %{tl_version}
Provides:       tex(udmj83.tfm) = %{tl_version}, tex(udmj84.tfm) = %{tl_version}
Provides:       tex(udmj85.tfm) = %{tl_version}, tex(udmj86.tfm) = %{tl_version}
Provides:       tex(udmj87.tfm) = %{tl_version}, tex(udmj88.tfm) = %{tl_version}
Provides:       tex(udmj89.tfm) = %{tl_version}, tex(udmj8a.tfm) = %{tl_version}
Provides:       tex(udmj8b.tfm) = %{tl_version}, tex(udmj8c.tfm) = %{tl_version}
Provides:       tex(udmj8d.tfm) = %{tl_version}, tex(udmj8e.tfm) = %{tl_version}
Provides:       tex(udmj8f.tfm) = %{tl_version}, tex(udmj90.tfm) = %{tl_version}
Provides:       tex(udmj91.tfm) = %{tl_version}, tex(udmj92.tfm) = %{tl_version}
Provides:       tex(udmj93.tfm) = %{tl_version}, tex(udmj94.tfm) = %{tl_version}
Provides:       tex(udmj95.tfm) = %{tl_version}, tex(udmj96.tfm) = %{tl_version}
Provides:       tex(udmj97.tfm) = %{tl_version}, tex(udmj98.tfm) = %{tl_version}
Provides:       tex(udmj99.tfm) = %{tl_version}, tex(udmj9a.tfm) = %{tl_version}
Provides:       tex(udmj9b.tfm) = %{tl_version}, tex(udmj9c.tfm) = %{tl_version}
Provides:       tex(udmj9d.tfm) = %{tl_version}, tex(udmj9e.tfm) = %{tl_version}
Provides:       tex(udmj9f.tfm) = %{tl_version}, tex(udmjff.tfm) = %{tl_version}
Provides:       tex(umcj00.tfm) = %{tl_version}, tex(umcj03.tfm) = %{tl_version}
Provides:       tex(umcj04.tfm) = %{tl_version}, tex(umcj20.tfm) = %{tl_version}
Provides:       tex(umcj21.tfm) = %{tl_version}, tex(umcj22.tfm) = %{tl_version}
Provides:       tex(umcj23.tfm) = %{tl_version}, tex(umcj25.tfm) = %{tl_version}
Provides:       tex(umcj26.tfm) = %{tl_version}, tex(umcj30.tfm) = %{tl_version}
Provides:       tex(umcj4e.tfm) = %{tl_version}, tex(umcj4f.tfm) = %{tl_version}
Provides:       tex(umcj50.tfm) = %{tl_version}, tex(umcj51.tfm) = %{tl_version}
Provides:       tex(umcj52.tfm) = %{tl_version}, tex(umcj53.tfm) = %{tl_version}
Provides:       tex(umcj54.tfm) = %{tl_version}, tex(umcj55.tfm) = %{tl_version}
Provides:       tex(umcj56.tfm) = %{tl_version}, tex(umcj57.tfm) = %{tl_version}
Provides:       tex(umcj58.tfm) = %{tl_version}, tex(umcj59.tfm) = %{tl_version}
Provides:       tex(umcj5a.tfm) = %{tl_version}, tex(umcj5b.tfm) = %{tl_version}
Provides:       tex(umcj5c.tfm) = %{tl_version}, tex(umcj5d.tfm) = %{tl_version}
Provides:       tex(umcj5e.tfm) = %{tl_version}, tex(umcj5f.tfm) = %{tl_version}
Provides:       tex(umcj60.tfm) = %{tl_version}, tex(umcj61.tfm) = %{tl_version}
Provides:       tex(umcj62.tfm) = %{tl_version}, tex(umcj63.tfm) = %{tl_version}
Provides:       tex(umcj64.tfm) = %{tl_version}, tex(umcj65.tfm) = %{tl_version}
Provides:       tex(umcj66.tfm) = %{tl_version}, tex(umcj67.tfm) = %{tl_version}
Provides:       tex(umcj68.tfm) = %{tl_version}, tex(umcj69.tfm) = %{tl_version}
Provides:       tex(umcj6a.tfm) = %{tl_version}, tex(umcj6b.tfm) = %{tl_version}
Provides:       tex(umcj6c.tfm) = %{tl_version}, tex(umcj6d.tfm) = %{tl_version}
Provides:       tex(umcj6e.tfm) = %{tl_version}, tex(umcj6f.tfm) = %{tl_version}
Provides:       tex(umcj70.tfm) = %{tl_version}, tex(umcj71.tfm) = %{tl_version}
Provides:       tex(umcj72.tfm) = %{tl_version}, tex(umcj73.tfm) = %{tl_version}
Provides:       tex(umcj74.tfm) = %{tl_version}, tex(umcj75.tfm) = %{tl_version}
Provides:       tex(umcj76.tfm) = %{tl_version}, tex(umcj77.tfm) = %{tl_version}
Provides:       tex(umcj78.tfm) = %{tl_version}, tex(umcj79.tfm) = %{tl_version}
Provides:       tex(umcj7a.tfm) = %{tl_version}, tex(umcj7b.tfm) = %{tl_version}
Provides:       tex(umcj7c.tfm) = %{tl_version}, tex(umcj7d.tfm) = %{tl_version}
Provides:       tex(umcj7e.tfm) = %{tl_version}, tex(umcj7f.tfm) = %{tl_version}
Provides:       tex(umcj80.tfm) = %{tl_version}, tex(umcj81.tfm) = %{tl_version}
Provides:       tex(umcj82.tfm) = %{tl_version}, tex(umcj83.tfm) = %{tl_version}
Provides:       tex(umcj84.tfm) = %{tl_version}, tex(umcj85.tfm) = %{tl_version}
Provides:       tex(umcj86.tfm) = %{tl_version}, tex(umcj87.tfm) = %{tl_version}
Provides:       tex(umcj88.tfm) = %{tl_version}, tex(umcj89.tfm) = %{tl_version}
Provides:       tex(umcj8a.tfm) = %{tl_version}, tex(umcj8b.tfm) = %{tl_version}
Provides:       tex(umcj8c.tfm) = %{tl_version}, tex(umcj8d.tfm) = %{tl_version}
Provides:       tex(umcj8e.tfm) = %{tl_version}, tex(umcj8f.tfm) = %{tl_version}
Provides:       tex(umcj90.tfm) = %{tl_version}, tex(umcj91.tfm) = %{tl_version}
Provides:       tex(umcj92.tfm) = %{tl_version}, tex(umcj93.tfm) = %{tl_version}
Provides:       tex(umcj94.tfm) = %{tl_version}, tex(umcj95.tfm) = %{tl_version}
Provides:       tex(umcj96.tfm) = %{tl_version}, tex(umcj97.tfm) = %{tl_version}
Provides:       tex(umcj98.tfm) = %{tl_version}, tex(umcj99.tfm) = %{tl_version}
Provides:       tex(umcj9a.tfm) = %{tl_version}, tex(umcj9b.tfm) = %{tl_version}
Provides:       tex(umcj9c.tfm) = %{tl_version}, tex(umcj9d.tfm) = %{tl_version}
Provides:       tex(umcj9e.tfm) = %{tl_version}, tex(umcj9f.tfm) = %{tl_version}
Provides:       tex(umcjff.tfm) = %{tl_version}, tex(umrj00.tfm) = %{tl_version}
Provides:       tex(umrj03.tfm) = %{tl_version}, tex(umrj04.tfm) = %{tl_version}
Provides:       tex(umrj20.tfm) = %{tl_version}, tex(umrj21.tfm) = %{tl_version}
Provides:       tex(umrj22.tfm) = %{tl_version}, tex(umrj23.tfm) = %{tl_version}
Provides:       tex(umrj25.tfm) = %{tl_version}, tex(umrj26.tfm) = %{tl_version}
Provides:       tex(umrj30.tfm) = %{tl_version}, tex(umrj4e.tfm) = %{tl_version}
Provides:       tex(umrj4f.tfm) = %{tl_version}, tex(umrj50.tfm) = %{tl_version}
Provides:       tex(umrj51.tfm) = %{tl_version}, tex(umrj52.tfm) = %{tl_version}
Provides:       tex(umrj53.tfm) = %{tl_version}, tex(umrj54.tfm) = %{tl_version}
Provides:       tex(umrj55.tfm) = %{tl_version}, tex(umrj56.tfm) = %{tl_version}
Provides:       tex(umrj57.tfm) = %{tl_version}, tex(umrj58.tfm) = %{tl_version}
Provides:       tex(umrj59.tfm) = %{tl_version}, tex(umrj5a.tfm) = %{tl_version}
Provides:       tex(umrj5b.tfm) = %{tl_version}, tex(umrj5c.tfm) = %{tl_version}
Provides:       tex(umrj5d.tfm) = %{tl_version}, tex(umrj5e.tfm) = %{tl_version}
Provides:       tex(umrj5f.tfm) = %{tl_version}, tex(umrj60.tfm) = %{tl_version}
Provides:       tex(umrj61.tfm) = %{tl_version}, tex(umrj62.tfm) = %{tl_version}
Provides:       tex(umrj63.tfm) = %{tl_version}, tex(umrj64.tfm) = %{tl_version}
Provides:       tex(umrj65.tfm) = %{tl_version}, tex(umrj66.tfm) = %{tl_version}
Provides:       tex(umrj67.tfm) = %{tl_version}, tex(umrj68.tfm) = %{tl_version}
Provides:       tex(umrj69.tfm) = %{tl_version}, tex(umrj6a.tfm) = %{tl_version}
Provides:       tex(umrj6b.tfm) = %{tl_version}, tex(umrj6c.tfm) = %{tl_version}
Provides:       tex(umrj6d.tfm) = %{tl_version}, tex(umrj6e.tfm) = %{tl_version}
Provides:       tex(umrj6f.tfm) = %{tl_version}, tex(umrj70.tfm) = %{tl_version}
Provides:       tex(umrj71.tfm) = %{tl_version}, tex(umrj72.tfm) = %{tl_version}
Provides:       tex(umrj73.tfm) = %{tl_version}, tex(umrj74.tfm) = %{tl_version}
Provides:       tex(umrj75.tfm) = %{tl_version}, tex(umrj76.tfm) = %{tl_version}
Provides:       tex(umrj77.tfm) = %{tl_version}, tex(umrj78.tfm) = %{tl_version}
Provides:       tex(umrj79.tfm) = %{tl_version}, tex(umrj7a.tfm) = %{tl_version}
Provides:       tex(umrj7b.tfm) = %{tl_version}, tex(umrj7c.tfm) = %{tl_version}
Provides:       tex(umrj7d.tfm) = %{tl_version}, tex(umrj7e.tfm) = %{tl_version}
Provides:       tex(umrj7f.tfm) = %{tl_version}, tex(umrj80.tfm) = %{tl_version}
Provides:       tex(umrj81.tfm) = %{tl_version}, tex(umrj82.tfm) = %{tl_version}
Provides:       tex(umrj83.tfm) = %{tl_version}, tex(umrj84.tfm) = %{tl_version}
Provides:       tex(umrj85.tfm) = %{tl_version}, tex(umrj86.tfm) = %{tl_version}
Provides:       tex(umrj87.tfm) = %{tl_version}, tex(umrj88.tfm) = %{tl_version}
Provides:       tex(umrj89.tfm) = %{tl_version}, tex(umrj8a.tfm) = %{tl_version}
Provides:       tex(umrj8b.tfm) = %{tl_version}, tex(umrj8c.tfm) = %{tl_version}
Provides:       tex(umrj8d.tfm) = %{tl_version}, tex(umrj8e.tfm) = %{tl_version}
Provides:       tex(umrj8f.tfm) = %{tl_version}, tex(umrj90.tfm) = %{tl_version}
Provides:       tex(umrj91.tfm) = %{tl_version}, tex(umrj92.tfm) = %{tl_version}
Provides:       tex(umrj93.tfm) = %{tl_version}, tex(umrj94.tfm) = %{tl_version}
Provides:       tex(umrj95.tfm) = %{tl_version}, tex(umrj96.tfm) = %{tl_version}
Provides:       tex(umrj97.tfm) = %{tl_version}, tex(umrj98.tfm) = %{tl_version}
Provides:       tex(umrj99.tfm) = %{tl_version}, tex(umrj9a.tfm) = %{tl_version}
Provides:       tex(umrj9b.tfm) = %{tl_version}, tex(umrj9c.tfm) = %{tl_version}
Provides:       tex(umrj9d.tfm) = %{tl_version}, tex(umrj9e.tfm) = %{tl_version}
Provides:       tex(umrj9f.tfm) = %{tl_version}, tex(umrjff.tfm) = %{tl_version}
Provides:       tex(dgjgreek.pfb) = %{tl_version}, tex(dgjhira.pfb) = %{tl_version}
Provides:       tex(dgjhw.pfb) = %{tl_version}, tex(dgjka.pfb) = %{tl_version}
Provides:       tex(dgjkata.pfb) = %{tl_version}, tex(dgjkb.pfb) = %{tl_version}
Provides:       tex(dgjkc.pfb) = %{tl_version}, tex(dgjkd.pfb) = %{tl_version}
Provides:       tex(dgjke.pfb) = %{tl_version}, tex(dgjkeisen.pfb) = %{tl_version}
Provides:       tex(dgjkf.pfb) = %{tl_version}, tex(dgjkg.pfb) = %{tl_version}
Provides:       tex(dgjkh.pfb) = %{tl_version}, tex(dgjki.pfb) = %{tl_version}
Provides:       tex(dgjkj.pfb) = %{tl_version}, tex(dgjkk.pfb) = %{tl_version}
Provides:       tex(dgjkl.pfb) = %{tl_version}, tex(dgjkm.pfb) = %{tl_version}
Provides:       tex(dgjkn.pfb) = %{tl_version}, tex(dgjko.pfb) = %{tl_version}
Provides:       tex(dgjkp.pfb) = %{tl_version}, tex(dgjkq.pfb) = %{tl_version}
Provides:       tex(dgjkr.pfb) = %{tl_version}, tex(dgjks.pfb) = %{tl_version}
Provides:       tex(dgjkt.pfb) = %{tl_version}, tex(dgjku.pfb) = %{tl_version}
Provides:       tex(dgjkv.pfb) = %{tl_version}, tex(dgjkw.pfb) = %{tl_version}
Provides:       tex(dgjkx.pfb) = %{tl_version}, tex(dgjky.pfb) = %{tl_version}
Provides:       tex(dgjkz.pfb) = %{tl_version}, tex(dgjroma.pfb) = %{tl_version}
Provides:       tex(dgjrussian.pfb) = %{tl_version}, tex(dgjsy.pfb) = %{tl_version}
Provides:       tex(dmjgreek.pfb) = %{tl_version}, tex(dmjhira.pfb) = %{tl_version}
Provides:       tex(dmjhw.pfb) = %{tl_version}, tex(dmjka.pfb) = %{tl_version}
Provides:       tex(dmjkata.pfb) = %{tl_version}, tex(dmjkb.pfb) = %{tl_version}
Provides:       tex(dmjkc.pfb) = %{tl_version}, tex(dmjkd.pfb) = %{tl_version}
Provides:       tex(dmjke.pfb) = %{tl_version}, tex(dmjkeisen.pfb) = %{tl_version}
Provides:       tex(dmjkf.pfb) = %{tl_version}, tex(dmjkg.pfb) = %{tl_version}
Provides:       tex(dmjkh.pfb) = %{tl_version}, tex(dmjki.pfb) = %{tl_version}
Provides:       tex(dmjkj.pfb) = %{tl_version}, tex(dmjkk.pfb) = %{tl_version}
Provides:       tex(dmjkl.pfb) = %{tl_version}, tex(dmjkm.pfb) = %{tl_version}
Provides:       tex(dmjkn.pfb) = %{tl_version}, tex(dmjko.pfb) = %{tl_version}
Provides:       tex(dmjkp.pfb) = %{tl_version}, tex(dmjkq.pfb) = %{tl_version}
Provides:       tex(dmjkr.pfb) = %{tl_version}, tex(dmjks.pfb) = %{tl_version}
Provides:       tex(dmjkt.pfb) = %{tl_version}, tex(dmjku.pfb) = %{tl_version}
Provides:       tex(dmjkv.pfb) = %{tl_version}, tex(dmjkw.pfb) = %{tl_version}
Provides:       tex(dmjkx.pfb) = %{tl_version}, tex(dmjky.pfb) = %{tl_version}
Provides:       tex(dmjkz.pfb) = %{tl_version}, tex(dmjroma.pfb) = %{tl_version}
Provides:       tex(dmjrussian.pfb) = %{tl_version}, tex(dmjsy.pfb) = %{tl_version}
Provides:       tex(mc2jka.pfb) = %{tl_version}, tex(mc2jkb.pfb) = %{tl_version}
Provides:       tex(mc2jkc.pfb) = %{tl_version}, tex(mc2jkd.pfb) = %{tl_version}
Provides:       tex(mc2jke.pfb) = %{tl_version}, tex(mc2jkf.pfb) = %{tl_version}
Provides:       tex(mc2jkg.pfb) = %{tl_version}, tex(mc2jkh.pfb) = %{tl_version}
Provides:       tex(mc2jki.pfb) = %{tl_version}, tex(mc2jkj.pfb) = %{tl_version}
Provides:       tex(mc2jkk.pfb) = %{tl_version}, tex(mc2jkl.pfb) = %{tl_version}
Provides:       tex(mc2jkm.pfb) = %{tl_version}, tex(mc2jkn.pfb) = %{tl_version}
Provides:       tex(mc2jko.pfb) = %{tl_version}, tex(mc2jkp.pfb) = %{tl_version}
Provides:       tex(mc2jkq.pfb) = %{tl_version}, tex(mc2jkr.pfb) = %{tl_version}
Provides:       tex(mc2jks.pfb) = %{tl_version}, tex(mc2jkt.pfb) = %{tl_version}
Provides:       tex(mc2jku.pfb) = %{tl_version}, tex(mc2jkv.pfb) = %{tl_version}
Provides:       tex(mc2jkw.pfb) = %{tl_version}, tex(mcjgreek.pfb) = %{tl_version}
Provides:       tex(mcjhira.pfb) = %{tl_version}, tex(mcjhw.pfb) = %{tl_version}
Provides:       tex(mcjka.pfb) = %{tl_version}, tex(mcjkata.pfb) = %{tl_version}
Provides:       tex(mcjkb.pfb) = %{tl_version}, tex(mcjkc.pfb) = %{tl_version}
Provides:       tex(mcjkd.pfb) = %{tl_version}, tex(mcjke.pfb) = %{tl_version}
Provides:       tex(mcjkeisen.pfb) = %{tl_version}, tex(mcjkf.pfb) = %{tl_version}
Provides:       tex(mcjkg.pfb) = %{tl_version}, tex(mcjkh.pfb) = %{tl_version}
Provides:       tex(mcjki.pfb) = %{tl_version}, tex(mcjkj.pfb) = %{tl_version}
Provides:       tex(mcjkk.pfb) = %{tl_version}, tex(mcjkl.pfb) = %{tl_version}
Provides:       tex(mcjkm.pfb) = %{tl_version}, tex(mcjkn.pfb) = %{tl_version}
Provides:       tex(mcjko.pfb) = %{tl_version}, tex(mcjkp.pfb) = %{tl_version}
Provides:       tex(mcjkq.pfb) = %{tl_version}, tex(mcjkr.pfb) = %{tl_version}
Provides:       tex(mcjks.pfb) = %{tl_version}, tex(mcjkt.pfb) = %{tl_version}
Provides:       tex(mcjku.pfb) = %{tl_version}, tex(mcjkv.pfb) = %{tl_version}
Provides:       tex(mcjkw.pfb) = %{tl_version}, tex(mcjkx.pfb) = %{tl_version}
Provides:       tex(mcjky.pfb) = %{tl_version}, tex(mcjkz.pfb) = %{tl_version}
Provides:       tex(mcjroma.pfb) = %{tl_version}, tex(mcjrussian.pfb) = %{tl_version}
Provides:       tex(mcjsy.pfb) = %{tl_version}, tex(mr2jka.pfb) = %{tl_version}
Provides:       tex(mr2jkb.pfb) = %{tl_version}, tex(mr2jkc.pfb) = %{tl_version}
Provides:       tex(mr2jkd.pfb) = %{tl_version}, tex(mr2jke.pfb) = %{tl_version}
Provides:       tex(mr2jkf.pfb) = %{tl_version}, tex(mr2jkg.pfb) = %{tl_version}
Provides:       tex(mr2jkh.pfb) = %{tl_version}, tex(mr2jki.pfb) = %{tl_version}
Provides:       tex(mr2jkj.pfb) = %{tl_version}, tex(mr2jkk.pfb) = %{tl_version}
Provides:       tex(mr2jkl.pfb) = %{tl_version}, tex(mr2jkm.pfb) = %{tl_version}
Provides:       tex(mr2jkn.pfb) = %{tl_version}, tex(mr2jko.pfb) = %{tl_version}
Provides:       tex(mr2jkp.pfb) = %{tl_version}, tex(mr2jkq.pfb) = %{tl_version}
Provides:       tex(mr2jkr.pfb) = %{tl_version}, tex(mr2jks.pfb) = %{tl_version}
Provides:       tex(mr2jkt.pfb) = %{tl_version}, tex(mr2jku.pfb) = %{tl_version}
Provides:       tex(mr2jkv.pfb) = %{tl_version}, tex(mr2jkw.pfb) = %{tl_version}
Provides:       tex(mrjgreek.pfb) = %{tl_version}, tex(mrjhira.pfb) = %{tl_version}
Provides:       tex(mrjhw.pfb) = %{tl_version}, tex(mrjka.pfb) = %{tl_version}
Provides:       tex(mrjkata.pfb) = %{tl_version}, tex(mrjkb.pfb) = %{tl_version}
Provides:       tex(mrjkc.pfb) = %{tl_version}, tex(mrjkd.pfb) = %{tl_version}
Provides:       tex(mrjke.pfb) = %{tl_version}, tex(mrjkeisen.pfb) = %{tl_version}
Provides:       tex(mrjkf.pfb) = %{tl_version}, tex(mrjkg.pfb) = %{tl_version}
Provides:       tex(mrjkh.pfb) = %{tl_version}, tex(mrjki.pfb) = %{tl_version}
Provides:       tex(mrjkj.pfb) = %{tl_version}, tex(mrjkk.pfb) = %{tl_version}
Provides:       tex(mrjkl.pfb) = %{tl_version}, tex(mrjkm.pfb) = %{tl_version}
Provides:       tex(mrjkn.pfb) = %{tl_version}, tex(mrjko.pfb) = %{tl_version}
Provides:       tex(mrjkp.pfb) = %{tl_version}, tex(mrjkq.pfb) = %{tl_version}
Provides:       tex(mrjkr.pfb) = %{tl_version}, tex(mrjks.pfb) = %{tl_version}
Provides:       tex(mrjkt.pfb) = %{tl_version}, tex(mrjku.pfb) = %{tl_version}
Provides:       tex(mrjkv.pfb) = %{tl_version}, tex(mrjkw.pfb) = %{tl_version}
Provides:       tex(mrjkx.pfb) = %{tl_version}, tex(mrjky.pfb) = %{tl_version}
Provides:       tex(mrjkz.pfb) = %{tl_version}, tex(mrjroma.pfb) = %{tl_version}
Provides:       tex(mrjrussian.pfb) = %{tl_version}, tex(mrjsy.pfb) = %{tl_version}
Provides:       tex(udgj00.vf) = %{tl_version}, tex(udgj03.vf) = %{tl_version}
Provides:       tex(udgj04.vf) = %{tl_version}, tex(udgj20.vf) = %{tl_version}
Provides:       tex(udgj21.vf) = %{tl_version}, tex(udgj22.vf) = %{tl_version}
Provides:       tex(udgj23.vf) = %{tl_version}, tex(udgj25.vf) = %{tl_version}
Provides:       tex(udgj26.vf) = %{tl_version}, tex(udgj30.vf) = %{tl_version}
Provides:       tex(udgj4e.vf) = %{tl_version}, tex(udgj4f.vf) = %{tl_version}
Provides:       tex(udgj50.vf) = %{tl_version}, tex(udgj51.vf) = %{tl_version}
Provides:       tex(udgj52.vf) = %{tl_version}, tex(udgj53.vf) = %{tl_version}
Provides:       tex(udgj54.vf) = %{tl_version}, tex(udgj55.vf) = %{tl_version}
Provides:       tex(udgj56.vf) = %{tl_version}, tex(udgj57.vf) = %{tl_version}
Provides:       tex(udgj58.vf) = %{tl_version}, tex(udgj59.vf) = %{tl_version}
Provides:       tex(udgj5a.vf) = %{tl_version}, tex(udgj5b.vf) = %{tl_version}
Provides:       tex(udgj5c.vf) = %{tl_version}, tex(udgj5d.vf) = %{tl_version}
Provides:       tex(udgj5e.vf) = %{tl_version}, tex(udgj5f.vf) = %{tl_version}
Provides:       tex(udgj60.vf) = %{tl_version}, tex(udgj61.vf) = %{tl_version}
Provides:       tex(udgj62.vf) = %{tl_version}, tex(udgj63.vf) = %{tl_version}
Provides:       tex(udgj64.vf) = %{tl_version}, tex(udgj65.vf) = %{tl_version}
Provides:       tex(udgj66.vf) = %{tl_version}, tex(udgj67.vf) = %{tl_version}
Provides:       tex(udgj68.vf) = %{tl_version}, tex(udgj69.vf) = %{tl_version}
Provides:       tex(udgj6a.vf) = %{tl_version}, tex(udgj6b.vf) = %{tl_version}
Provides:       tex(udgj6c.vf) = %{tl_version}, tex(udgj6d.vf) = %{tl_version}
Provides:       tex(udgj6e.vf) = %{tl_version}, tex(udgj6f.vf) = %{tl_version}
Provides:       tex(udgj70.vf) = %{tl_version}, tex(udgj71.vf) = %{tl_version}
Provides:       tex(udgj72.vf) = %{tl_version}, tex(udgj73.vf) = %{tl_version}
Provides:       tex(udgj74.vf) = %{tl_version}, tex(udgj75.vf) = %{tl_version}
Provides:       tex(udgj76.vf) = %{tl_version}, tex(udgj77.vf) = %{tl_version}
Provides:       tex(udgj78.vf) = %{tl_version}, tex(udgj79.vf) = %{tl_version}
Provides:       tex(udgj7a.vf) = %{tl_version}, tex(udgj7b.vf) = %{tl_version}
Provides:       tex(udgj7c.vf) = %{tl_version}, tex(udgj7d.vf) = %{tl_version}
Provides:       tex(udgj7e.vf) = %{tl_version}, tex(udgj7f.vf) = %{tl_version}
Provides:       tex(udgj80.vf) = %{tl_version}, tex(udgj81.vf) = %{tl_version}
Provides:       tex(udgj82.vf) = %{tl_version}, tex(udgj83.vf) = %{tl_version}
Provides:       tex(udgj84.vf) = %{tl_version}, tex(udgj85.vf) = %{tl_version}
Provides:       tex(udgj86.vf) = %{tl_version}, tex(udgj87.vf) = %{tl_version}
Provides:       tex(udgj88.vf) = %{tl_version}, tex(udgj89.vf) = %{tl_version}
Provides:       tex(udgj8a.vf) = %{tl_version}, tex(udgj8b.vf) = %{tl_version}
Provides:       tex(udgj8c.vf) = %{tl_version}, tex(udgj8d.vf) = %{tl_version}
Provides:       tex(udgj8e.vf) = %{tl_version}, tex(udgj8f.vf) = %{tl_version}
Provides:       tex(udgj90.vf) = %{tl_version}, tex(udgj91.vf) = %{tl_version}
Provides:       tex(udgj92.vf) = %{tl_version}, tex(udgj93.vf) = %{tl_version}
Provides:       tex(udgj94.vf) = %{tl_version}, tex(udgj95.vf) = %{tl_version}
Provides:       tex(udgj96.vf) = %{tl_version}, tex(udgj97.vf) = %{tl_version}
Provides:       tex(udgj98.vf) = %{tl_version}, tex(udgj99.vf) = %{tl_version}
Provides:       tex(udgj9a.vf) = %{tl_version}, tex(udgj9b.vf) = %{tl_version}
Provides:       tex(udgj9c.vf) = %{tl_version}, tex(udgj9d.vf) = %{tl_version}
Provides:       tex(udgj9e.vf) = %{tl_version}, tex(udgj9f.vf) = %{tl_version}
Provides:       tex(udgjff.vf) = %{tl_version}, tex(udmj00.vf) = %{tl_version}
Provides:       tex(udmj03.vf) = %{tl_version}, tex(udmj04.vf) = %{tl_version}
Provides:       tex(udmj20.vf) = %{tl_version}, tex(udmj21.vf) = %{tl_version}
Provides:       tex(udmj22.vf) = %{tl_version}, tex(udmj23.vf) = %{tl_version}
Provides:       tex(udmj25.vf) = %{tl_version}, tex(udmj26.vf) = %{tl_version}
Provides:       tex(udmj30.vf) = %{tl_version}, tex(udmj4e.vf) = %{tl_version}
Provides:       tex(udmj4f.vf) = %{tl_version}, tex(udmj50.vf) = %{tl_version}
Provides:       tex(udmj51.vf) = %{tl_version}, tex(udmj52.vf) = %{tl_version}
Provides:       tex(udmj53.vf) = %{tl_version}, tex(udmj54.vf) = %{tl_version}
Provides:       tex(udmj55.vf) = %{tl_version}, tex(udmj56.vf) = %{tl_version}
Provides:       tex(udmj57.vf) = %{tl_version}, tex(udmj58.vf) = %{tl_version}
Provides:       tex(udmj59.vf) = %{tl_version}, tex(udmj5a.vf) = %{tl_version}
Provides:       tex(udmj5b.vf) = %{tl_version}, tex(udmj5c.vf) = %{tl_version}
Provides:       tex(udmj5d.vf) = %{tl_version}, tex(udmj5e.vf) = %{tl_version}
Provides:       tex(udmj5f.vf) = %{tl_version}, tex(udmj60.vf) = %{tl_version}
Provides:       tex(udmj61.vf) = %{tl_version}, tex(udmj62.vf) = %{tl_version}
Provides:       tex(udmj63.vf) = %{tl_version}, tex(udmj64.vf) = %{tl_version}
Provides:       tex(udmj65.vf) = %{tl_version}, tex(udmj66.vf) = %{tl_version}
Provides:       tex(udmj67.vf) = %{tl_version}, tex(udmj68.vf) = %{tl_version}
Provides:       tex(udmj69.vf) = %{tl_version}, tex(udmj6a.vf) = %{tl_version}
Provides:       tex(udmj6b.vf) = %{tl_version}, tex(udmj6c.vf) = %{tl_version}
Provides:       tex(udmj6d.vf) = %{tl_version}, tex(udmj6e.vf) = %{tl_version}
Provides:       tex(udmj6f.vf) = %{tl_version}, tex(udmj70.vf) = %{tl_version}
Provides:       tex(udmj71.vf) = %{tl_version}, tex(udmj72.vf) = %{tl_version}
Provides:       tex(udmj73.vf) = %{tl_version}, tex(udmj74.vf) = %{tl_version}
Provides:       tex(udmj75.vf) = %{tl_version}, tex(udmj76.vf) = %{tl_version}
Provides:       tex(udmj77.vf) = %{tl_version}, tex(udmj78.vf) = %{tl_version}
Provides:       tex(udmj79.vf) = %{tl_version}, tex(udmj7a.vf) = %{tl_version}
Provides:       tex(udmj7b.vf) = %{tl_version}, tex(udmj7c.vf) = %{tl_version}
Provides:       tex(udmj7d.vf) = %{tl_version}, tex(udmj7e.vf) = %{tl_version}
Provides:       tex(udmj7f.vf) = %{tl_version}, tex(udmj80.vf) = %{tl_version}
Provides:       tex(udmj81.vf) = %{tl_version}, tex(udmj82.vf) = %{tl_version}
Provides:       tex(udmj83.vf) = %{tl_version}, tex(udmj84.vf) = %{tl_version}
Provides:       tex(udmj85.vf) = %{tl_version}, tex(udmj86.vf) = %{tl_version}
Provides:       tex(udmj87.vf) = %{tl_version}, tex(udmj88.vf) = %{tl_version}
Provides:       tex(udmj89.vf) = %{tl_version}, tex(udmj8a.vf) = %{tl_version}
Provides:       tex(udmj8b.vf) = %{tl_version}, tex(udmj8c.vf) = %{tl_version}
Provides:       tex(udmj8d.vf) = %{tl_version}, tex(udmj8e.vf) = %{tl_version}
Provides:       tex(udmj8f.vf) = %{tl_version}, tex(udmj90.vf) = %{tl_version}
Provides:       tex(udmj91.vf) = %{tl_version}, tex(udmj92.vf) = %{tl_version}
Provides:       tex(udmj93.vf) = %{tl_version}, tex(udmj94.vf) = %{tl_version}
Provides:       tex(udmj95.vf) = %{tl_version}, tex(udmj96.vf) = %{tl_version}
Provides:       tex(udmj97.vf) = %{tl_version}, tex(udmj98.vf) = %{tl_version}
Provides:       tex(udmj99.vf) = %{tl_version}, tex(udmj9a.vf) = %{tl_version}
Provides:       tex(udmj9b.vf) = %{tl_version}, tex(udmj9c.vf) = %{tl_version}
Provides:       tex(udmj9d.vf) = %{tl_version}, tex(udmj9e.vf) = %{tl_version}
Provides:       tex(udmj9f.vf) = %{tl_version}, tex(udmjff.vf) = %{tl_version}
Provides:       tex(umcj00.vf) = %{tl_version}, tex(umcj03.vf) = %{tl_version}
Provides:       tex(umcj04.vf) = %{tl_version}, tex(umcj20.vf) = %{tl_version}
Provides:       tex(umcj21.vf) = %{tl_version}, tex(umcj22.vf) = %{tl_version}
Provides:       tex(umcj23.vf) = %{tl_version}, tex(umcj25.vf) = %{tl_version}
Provides:       tex(umcj26.vf) = %{tl_version}, tex(umcj30.vf) = %{tl_version}
Provides:       tex(umcj4e.vf) = %{tl_version}, tex(umcj4f.vf) = %{tl_version}
Provides:       tex(umcj50.vf) = %{tl_version}, tex(umcj51.vf) = %{tl_version}
Provides:       tex(umcj52.vf) = %{tl_version}, tex(umcj53.vf) = %{tl_version}
Provides:       tex(umcj54.vf) = %{tl_version}, tex(umcj55.vf) = %{tl_version}
Provides:       tex(umcj56.vf) = %{tl_version}, tex(umcj57.vf) = %{tl_version}
Provides:       tex(umcj58.vf) = %{tl_version}, tex(umcj59.vf) = %{tl_version}
Provides:       tex(umcj5a.vf) = %{tl_version}, tex(umcj5b.vf) = %{tl_version}
Provides:       tex(umcj5c.vf) = %{tl_version}, tex(umcj5d.vf) = %{tl_version}
Provides:       tex(umcj5e.vf) = %{tl_version}, tex(umcj5f.vf) = %{tl_version}
Provides:       tex(umcj60.vf) = %{tl_version}, tex(umcj61.vf) = %{tl_version}
Provides:       tex(umcj62.vf) = %{tl_version}, tex(umcj63.vf) = %{tl_version}
Provides:       tex(umcj64.vf) = %{tl_version}, tex(umcj65.vf) = %{tl_version}
Provides:       tex(umcj66.vf) = %{tl_version}, tex(umcj67.vf) = %{tl_version}
Provides:       tex(umcj68.vf) = %{tl_version}, tex(umcj69.vf) = %{tl_version}
Provides:       tex(umcj6a.vf) = %{tl_version}, tex(umcj6b.vf) = %{tl_version}
Provides:       tex(umcj6c.vf) = %{tl_version}, tex(umcj6d.vf) = %{tl_version}
Provides:       tex(umcj6e.vf) = %{tl_version}, tex(umcj6f.vf) = %{tl_version}
Provides:       tex(umcj70.vf) = %{tl_version}, tex(umcj71.vf) = %{tl_version}
Provides:       tex(umcj72.vf) = %{tl_version}, tex(umcj73.vf) = %{tl_version}
Provides:       tex(umcj74.vf) = %{tl_version}, tex(umcj75.vf) = %{tl_version}
Provides:       tex(umcj76.vf) = %{tl_version}, tex(umcj77.vf) = %{tl_version}
Provides:       tex(umcj78.vf) = %{tl_version}, tex(umcj79.vf) = %{tl_version}
Provides:       tex(umcj7a.vf) = %{tl_version}, tex(umcj7b.vf) = %{tl_version}
Provides:       tex(umcj7c.vf) = %{tl_version}, tex(umcj7d.vf) = %{tl_version}
Provides:       tex(umcj7e.vf) = %{tl_version}, tex(umcj7f.vf) = %{tl_version}
Provides:       tex(umcj80.vf) = %{tl_version}, tex(umcj81.vf) = %{tl_version}
Provides:       tex(umcj82.vf) = %{tl_version}, tex(umcj83.vf) = %{tl_version}
Provides:       tex(umcj84.vf) = %{tl_version}, tex(umcj85.vf) = %{tl_version}
Provides:       tex(umcj86.vf) = %{tl_version}, tex(umcj87.vf) = %{tl_version}
Provides:       tex(umcj88.vf) = %{tl_version}, tex(umcj89.vf) = %{tl_version}
Provides:       tex(umcj8a.vf) = %{tl_version}, tex(umcj8b.vf) = %{tl_version}
Provides:       tex(umcj8c.vf) = %{tl_version}, tex(umcj8d.vf) = %{tl_version}
Provides:       tex(umcj8e.vf) = %{tl_version}, tex(umcj8f.vf) = %{tl_version}
Provides:       tex(umcj90.vf) = %{tl_version}, tex(umcj91.vf) = %{tl_version}
Provides:       tex(umcj92.vf) = %{tl_version}, tex(umcj93.vf) = %{tl_version}
Provides:       tex(umcj94.vf) = %{tl_version}, tex(umcj95.vf) = %{tl_version}
Provides:       tex(umcj96.vf) = %{tl_version}, tex(umcj97.vf) = %{tl_version}
Provides:       tex(umcj98.vf) = %{tl_version}, tex(umcj99.vf) = %{tl_version}
Provides:       tex(umcj9a.vf) = %{tl_version}, tex(umcj9b.vf) = %{tl_version}
Provides:       tex(umcj9c.vf) = %{tl_version}, tex(umcj9d.vf) = %{tl_version}
Provides:       tex(umcj9e.vf) = %{tl_version}, tex(umcj9f.vf) = %{tl_version}
Provides:       tex(umcjff.vf) = %{tl_version}, tex(umrj00.vf) = %{tl_version}
Provides:       tex(umrj03.vf) = %{tl_version}, tex(umrj04.vf) = %{tl_version}
Provides:       tex(umrj20.vf) = %{tl_version}, tex(umrj21.vf) = %{tl_version}
Provides:       tex(umrj22.vf) = %{tl_version}, tex(umrj23.vf) = %{tl_version}
Provides:       tex(umrj25.vf) = %{tl_version}, tex(umrj26.vf) = %{tl_version}
Provides:       tex(umrj30.vf) = %{tl_version}, tex(umrj4e.vf) = %{tl_version}
Provides:       tex(umrj4f.vf) = %{tl_version}, tex(umrj50.vf) = %{tl_version}
Provides:       tex(umrj51.vf) = %{tl_version}, tex(umrj52.vf) = %{tl_version}
Provides:       tex(umrj53.vf) = %{tl_version}, tex(umrj54.vf) = %{tl_version}
Provides:       tex(umrj55.vf) = %{tl_version}, tex(umrj56.vf) = %{tl_version}
Provides:       tex(umrj57.vf) = %{tl_version}, tex(umrj58.vf) = %{tl_version}
Provides:       tex(umrj59.vf) = %{tl_version}, tex(umrj5a.vf) = %{tl_version}
Provides:       tex(umrj5b.vf) = %{tl_version}, tex(umrj5c.vf) = %{tl_version}
Provides:       tex(umrj5d.vf) = %{tl_version}, tex(umrj5e.vf) = %{tl_version}
Provides:       tex(umrj5f.vf) = %{tl_version}, tex(umrj60.vf) = %{tl_version}
Provides:       tex(umrj61.vf) = %{tl_version}, tex(umrj62.vf) = %{tl_version}
Provides:       tex(umrj63.vf) = %{tl_version}, tex(umrj64.vf) = %{tl_version}
Provides:       tex(umrj65.vf) = %{tl_version}, tex(umrj66.vf) = %{tl_version}
Provides:       tex(umrj67.vf) = %{tl_version}, tex(umrj68.vf) = %{tl_version}
Provides:       tex(umrj69.vf) = %{tl_version}, tex(umrj6a.vf) = %{tl_version}
Provides:       tex(umrj6b.vf) = %{tl_version}, tex(umrj6c.vf) = %{tl_version}
Provides:       tex(umrj6d.vf) = %{tl_version}, tex(umrj6e.vf) = %{tl_version}
Provides:       tex(umrj6f.vf) = %{tl_version}, tex(umrj70.vf) = %{tl_version}
Provides:       tex(umrj71.vf) = %{tl_version}, tex(umrj72.vf) = %{tl_version}
Provides:       tex(umrj73.vf) = %{tl_version}, tex(umrj74.vf) = %{tl_version}
Provides:       tex(umrj75.vf) = %{tl_version}, tex(umrj76.vf) = %{tl_version}
Provides:       tex(umrj77.vf) = %{tl_version}, tex(umrj78.vf) = %{tl_version}
Provides:       tex(umrj79.vf) = %{tl_version}, tex(umrj7a.vf) = %{tl_version}
Provides:       tex(umrj7b.vf) = %{tl_version}, tex(umrj7c.vf) = %{tl_version}
Provides:       tex(umrj7d.vf) = %{tl_version}, tex(umrj7e.vf) = %{tl_version}
Provides:       tex(umrj7f.vf) = %{tl_version}, tex(umrj80.vf) = %{tl_version}
Provides:       tex(umrj81.vf) = %{tl_version}, tex(umrj82.vf) = %{tl_version}
Provides:       tex(umrj83.vf) = %{tl_version}, tex(umrj84.vf) = %{tl_version}
Provides:       tex(umrj85.vf) = %{tl_version}, tex(umrj86.vf) = %{tl_version}
Provides:       tex(umrj87.vf) = %{tl_version}, tex(umrj88.vf) = %{tl_version}
Provides:       tex(umrj89.vf) = %{tl_version}, tex(umrj8a.vf) = %{tl_version}
Provides:       tex(umrj8b.vf) = %{tl_version}, tex(umrj8c.vf) = %{tl_version}
Provides:       tex(umrj8d.vf) = %{tl_version}, tex(umrj8e.vf) = %{tl_version}
Provides:       tex(umrj8f.vf) = %{tl_version}, tex(umrj90.vf) = %{tl_version}
Provides:       tex(umrj91.vf) = %{tl_version}, tex(umrj92.vf) = %{tl_version}
Provides:       tex(umrj93.vf) = %{tl_version}, tex(umrj94.vf) = %{tl_version}
Provides:       tex(umrj95.vf) = %{tl_version}, tex(umrj96.vf) = %{tl_version}
Provides:       tex(umrj97.vf) = %{tl_version}, tex(umrj98.vf) = %{tl_version}
Provides:       tex(umrj99.vf) = %{tl_version}, tex(umrj9a.vf) = %{tl_version}
Provides:       tex(umrj9b.vf) = %{tl_version}, tex(umrj9c.vf) = %{tl_version}
Provides:       tex(umrj9d.vf) = %{tl_version}, tex(umrj9e.vf) = %{tl_version}
Provides:       tex(umrj9f.vf) = %{tl_version}, tex(umrjff.vf) = %{tl_version}

%description -n texlive-wadalab
These are font bundles for the Japanese Wadalab fonts which
work with the CJK package. All subfonts now have glyph names
compliant to the Adobe Glyph List, making ToUnicode CMaps in
PDF documents (created automatically by dvipdfmx) work
correctly. All font bundles now contain virtual Unicode
subfonts.

%package -n texlive-wadalab-doc
Summary:        Documentation for wadalab
Version:        svn42428
Provides:       tex-wadalab-doc
AutoReqProv:    No

%description -n texlive-wadalab-doc
Documentation for wadalab

%package -n texlive-wnri
Provides:       tex-wnri = %{tl_version}
License:        GPL+
Summary:        Ridgeway's fonts
Version:        svn22459.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(wnindic.map) = %{tl_version}, tex(wnrib10.tfm) = %{tl_version}
Provides:       tex(wnrib8.tfm) = %{tl_version}, tex(wnribi10.tfm) = %{tl_version}
Provides:       tex(wnrii10.tfm) = %{tl_version}, tex(wnrii8.tfm) = %{tl_version}
Provides:       tex(wnrir10.tfm) = %{tl_version}, tex(wnrir8.tfm) = %{tl_version}
Provides:       tex(wnris10.tfm) = %{tl_version}, tex(wnris8.tfm) = %{tl_version}
Provides:       tex(wnrit10.tfm) = %{tl_version}, tex(wnrit8.tfm) = %{tl_version}

%description -n texlive-wnri
Fonts (as Metafont source) for Old English, Indic languages in
Roman transliteration and Puget Salish (Lushootseed) and other
Native American languages.

%package -n texlive-wnri-doc
Summary:        Documentation for wnri
Version:        svn22459.0

Provides:       tex-wnri-doc
AutoReqProv:    No

%description -n texlive-wnri-doc
Documentation for wnri

%package -n texlive-wnri-latex
Provides:       tex-wnri-latex = %{tl_version}
License:        GPLv2+
Summary:        LaTeX support for wnri fonts
Version:        svn22338.1.0b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ot1wnr.fd) = %{tl_version}, tex(ot1wnss.fd) = %{tl_version}
Provides:       tex(ot1wntt.fd) = %{tl_version}, tex(wnri.def) = %{tl_version}
Provides:       tex(wnri.sty) = %{tl_version}

%description -n texlive-wnri-latex
LaTeX support for the wnri fonts.

%package -n texlive-wnri-latex-doc
Summary:        Documentation for wnri-latex
Version:        svn22338.1.0b

Provides:       tex-wnri-latex-doc
AutoReqProv:    No

%description -n texlive-wnri-latex-doc
Documentation for wnri-latex

%package -n texlive-url
Provides:       tex-url = %{tl_version}
License:        LPPL
Summary:        Verbatim with URL-sensitive line breaks
Version:        svn32528.3.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(url.sty) = %{tl_version}

%description -n texlive-url
The command \url is a form of verbatim command that allows
linebreaks at certain characters or combinations of characters,
accepts reconfiguration, and can usually be used in the
argument to another command. (The \urldef command provides
robust commands that serve in cases when \url doesn't work in
an argument.) The command is intended for email addresses,
hypertext links, directories/paths, etc., which normally have
no spaces, so by default the package ignores spaces in its
argument. However, a package option "allows spaces", which is
useful for operating systems where spaces are a common part of
file names.

%package -n texlive-url-doc
Summary:        Documentation for url
Version:        svn32528.3.4

Provides:       tex-url-doc
AutoReqProv:    No

%description -n texlive-url-doc
Documentation for url

%package -n texlive-uni-wtal-ger
Provides:       tex-uni-wtal-ger = %{tl_version}
License:        LPPL 1.3
Summary:        Citation style for literary studies at the University of Wuppertal
Version:        svn31541.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(authortitle-dw.bbx), tex(authortitle-dw.cbx)
Provides:       tex(uni-wtal-ger.bbx) = %{tl_version}, tex(uni-wtal-ger.cbx) = %{tl_version}

%description -n texlive-uni-wtal-ger
The package defines a biblatex citation style based on the
author-title style of biblatex-dw. The citations are optimised
for literary studies in faculty of humanities at the Bergische
Universitat Wuppertal.

%package -n texlive-uni-wtal-ger-doc
Summary:        Documentation for uni-wtal-ger
Version:        svn31541.0.2

Provides:       tex-uni-wtal-ger-doc
AutoReqProv:    No

%description -n texlive-uni-wtal-ger-doc
Documentation for uni-wtal-ger

%package -n texlive-uni-wtal-lin
Provides:       tex-uni-wtal-lin = %{tl_version}
License:        LPPL 1.3
Summary:        Citation style for linguistic studies at the University of Wuppertal
Version:        svn31409.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(authoryear.bbx), tex(authoryear.cbx)
Provides:       tex(uni-wtal-lin.bbx) = %{tl_version}, tex(uni-wtal-lin.cbx) = %{tl_version}

%description -n texlive-uni-wtal-lin
The package defines a biblatex citation style based on the
standard author-year style. The citations are optimised for
linguistic studies at the Institute of Linguistics at the
Bergische Universitat Wuppertal.

%package -n texlive-uni-wtal-lin-doc
Summary:        Documentation for uni-wtal-lin
Version:        svn31409.0.2

Provides:       tex-uni-wtal-lin-doc
AutoReqProv:    No

%description -n texlive-uni-wtal-lin-doc
Documentation for uni-wtal-lin

%package -n texlive-usebib
Provides:       tex-usebib = %{tl_version}
License:        LPPL 1.3
Summary:        A simple bibliography processor
Version:        svn25969.1.0a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(url.sty), tex(keyval.sty)
Provides:       tex(usebib.sty) = %{tl_version}

%description -n texlive-usebib
The package is described by its author as "a poor person's
replacement for the more powerful methods provided by biblatex
to access data from a .bib file". Its principle commands are
\bibinput (which specifies a database to use) and \usebibdata
(which typesets a single field from a specified entry in that
database.

%package -n texlive-usebib-doc
Summary:        Documentation for usebib
Version:        svn25969.1.0a

Provides:       tex-usebib-doc
AutoReqProv:    No

%description -n texlive-usebib-doc
Documentation for usebib

%package -n texlive-vak
Provides:       tex-vak = %{tl_version}
License:        LPPL
Summary:        BibTeX style for Russian Theses, books, etc
Version:        svn23431.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-vak
The file can be used to format the bibliographies of PhD
theses, books etc., according to the latest Russian standards:
GOST 7.82 - 2001 and GOST 7.1 - 2003. It introduces the minimum
number of new entries and styles to cover all frequently used
situations. The style file provides an easy way to perform a
semiautomatic, or a completely manual sort of the list of the
references. Processing bibliographies produced by the style
requires a 8-bit BibTeX system.

%package -n texlive-vak-doc
Summary:        Documentation for vak
Version:        svn23431.0

Provides:       tex-vak-doc
AutoReqProv:    No

%description -n texlive-vak-doc
Documentation for vak

%package -n texlive-vntex
Provides:       tex-vntex = %{tl_version}
License:        Utopia
Summary:        Support for Vietnamese
Version:        svn30579.3.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(ifthen.sty), tex(ucs.sty), tex(ifpdf.sty), tex(cmap.sty)
Requires:       tex(fontenc.sty), tex(inputenc.sty)
Provides:       tex(t5.enc) = %{tl_version}, tex(t5d.enc) = %{tl_version}
Provides:       tex(t5uni.enc) = %{tl_version}, tex(arevvn.map) = %{tl_version}
Provides:       tex(chartervn.map) = %{tl_version}, tex(cmbrightvn.map) = %{tl_version}
Provides:       tex(concretevn.map) = %{tl_version}, tex(grotesqvn.map) = %{tl_version}
Provides:       tex(txttvn.map) = %{tl_version}, tex(urwvn.map) = %{tl_version}
Provides:       tex(vnrother.map) = %{tl_version}, tex(vnrtext.map) = %{tl_version}
Provides:       tex(vntopia.map) = %{tl_version}, tex(favb8v.tfm) = %{tl_version}
Provides:       tex(favbi8v.tfm) = %{tl_version}, tex(favr8v.tfm) = %{tl_version}
Provides:       tex(favri8v.tfm) = %{tl_version}, tex(bchb8v.tfm) = %{tl_version}
Provides:       tex(bchbc8v.tfm) = %{tl_version}, tex(bchbi8v.tfm) = %{tl_version}
Provides:       tex(bchbo8v.tfm) = %{tl_version}, tex(bchr8v.tfm) = %{tl_version}
Provides:       tex(bchrc8v.tfm) = %{tl_version}, tex(bchri8v.tfm) = %{tl_version}
Provides:       tex(bchro8v.tfm) = %{tl_version}, tex(vncmbr10.tfm) = %{tl_version}
Provides:       tex(vncmbr17.tfm) = %{tl_version}, tex(vncmbr8.tfm) = %{tl_version}
Provides:       tex(vncmbr9.tfm) = %{tl_version}, tex(vncmbrbx10.tfm) = %{tl_version}
Provides:       tex(vncmbrsl10.tfm) = %{tl_version}, tex(vncmbrsl17.tfm) = %{tl_version}
Provides:       tex(vncmbrsl8.tfm) = %{tl_version}, tex(vncmbrsl9.tfm) = %{tl_version}
Provides:       tex(vncmsltl10.tfm) = %{tl_version}, tex(vncmtl10.tfm) = %{tl_version}
Provides:       tex(vncccsc10.tfm) = %{tl_version}, tex(vnccr10.tfm) = %{tl_version}
Provides:       tex(vnccsl10.tfm) = %{tl_version}, tex(vnccti10.tfm) = %{tl_version}
Provides:       tex(ugqb8v.tfm) = %{tl_version}, tex(ugqbo8v.tfm) = %{tl_version}
Provides:       tex(txbtt8v.tfm) = %{tl_version}, tex(txbttsc8v.tfm) = %{tl_version}
Provides:       tex(txbttsl8v.tfm) = %{tl_version}, tex(txtt8v.tfm) = %{tl_version}
Provides:       tex(txttsc8v.tfm) = %{tl_version}, tex(txttsl8v.tfm) = %{tl_version}
Provides:       tex(fplrc8v.tfm) = %{tl_version}, tex(uagd8v.tfm) = %{tl_version}
Provides:       tex(uagdc8v.tfm) = %{tl_version}, tex(uagdo8v.tfm) = %{tl_version}
Provides:       tex(uagk8v.tfm) = %{tl_version}, tex(uagkc8v.tfm) = %{tl_version}
Provides:       tex(uagko8v.tfm) = %{tl_version}, tex(ubkd8v.tfm) = %{tl_version}
Provides:       tex(ubkdc8v.tfm) = %{tl_version}, tex(ubkdi8v.tfm) = %{tl_version}
Provides:       tex(ubkdo8v.tfm) = %{tl_version}, tex(ubkl8v.tfm) = %{tl_version}
Provides:       tex(ubklc8v.tfm) = %{tl_version}, tex(ubkli8v.tfm) = %{tl_version}
Provides:       tex(ubklo8v.tfm) = %{tl_version}, tex(ucrb8v.tfm) = %{tl_version}
Provides:       tex(ucrbc8v.tfm) = %{tl_version}, tex(ucrbo8v.tfm) = %{tl_version}
Provides:       tex(ucrr8v.tfm) = %{tl_version}, tex(ucrrc8v.tfm) = %{tl_version}
Provides:       tex(ucrro8v.tfm) = %{tl_version}, tex(uhvb8v.tfm) = %{tl_version}
Provides:       tex(uhvbc8v.tfm) = %{tl_version}, tex(uhvbo8v.tfm) = %{tl_version}
Provides:       tex(uhvr8v.tfm) = %{tl_version}, tex(uhvrc8v.tfm) = %{tl_version}
Provides:       tex(uhvro8v.tfm) = %{tl_version}, tex(uncb8v.tfm) = %{tl_version}
Provides:       tex(uncbc8v.tfm) = %{tl_version}, tex(uncbi8v.tfm) = %{tl_version}
Provides:       tex(uncbo8v.tfm) = %{tl_version}, tex(uncr8v.tfm) = %{tl_version}
Provides:       tex(uncrc8v.tfm) = %{tl_version}, tex(uncri8v.tfm) = %{tl_version}
Provides:       tex(uncro8v.tfm) = %{tl_version}, tex(uplb8v.tfm) = %{tl_version}
Provides:       tex(uplbc8v.tfm) = %{tl_version}, tex(uplbi8v.tfm) = %{tl_version}
Provides:       tex(uplbo8v.tfm) = %{tl_version}, tex(uplr8v.tfm) = %{tl_version}
Provides:       tex(uplrc8v.tfm) = %{tl_version}, tex(uplri8v.tfm) = %{tl_version}
Provides:       tex(uplro8v.tfm) = %{tl_version}, tex(utmb8v.tfm) = %{tl_version}
Provides:       tex(utmbc8v.tfm) = %{tl_version}, tex(utmbi8v.tfm) = %{tl_version}
Provides:       tex(utmbo8v.tfm) = %{tl_version}, tex(utmr8v.tfm) = %{tl_version}
Provides:       tex(utmrc8v.tfm) = %{tl_version}, tex(utmri8v.tfm) = %{tl_version}
Provides:       tex(utmro8v.tfm) = %{tl_version}, tex(uzcmi8v.tfm) = %{tl_version}
Provides:       tex(vnb10.tfm) = %{tl_version}, tex(vnbx10.tfm) = %{tl_version}
Provides:       tex(vnbx12.tfm) = %{tl_version}, tex(vnbx5.tfm) = %{tl_version}
Provides:       tex(vnbx6.tfm) = %{tl_version}, tex(vnbx7.tfm) = %{tl_version}
Provides:       tex(vnbx8.tfm) = %{tl_version}, tex(vnbx9.tfm) = %{tl_version}
Provides:       tex(vnbxsl10.tfm) = %{tl_version}, tex(vnbxti10.tfm) = %{tl_version}
Provides:       tex(vncsc10.tfm) = %{tl_version}, tex(vndunh10.tfm) = %{tl_version}
Provides:       tex(vnff10.tfm) = %{tl_version}, tex(vnfi10.tfm) = %{tl_version}
Provides:       tex(vnfib8.tfm) = %{tl_version}, tex(vnitt10.tfm) = %{tl_version}
Provides:       tex(vnr10.tfm) = %{tl_version}, tex(vnr12.tfm) = %{tl_version}
Provides:       tex(vnr17.tfm) = %{tl_version}, tex(vnr5.tfm) = %{tl_version}
Provides:       tex(vnr6.tfm) = %{tl_version}, tex(vnr7.tfm) = %{tl_version}
Provides:       tex(vnr8.tfm) = %{tl_version}, tex(vnr9.tfm) = %{tl_version}
Provides:       tex(vnsl10.tfm) = %{tl_version}, tex(vnsl12.tfm) = %{tl_version}
Provides:       tex(vnsl8.tfm) = %{tl_version}, tex(vnsl9.tfm) = %{tl_version}
Provides:       tex(vnsltt10.tfm) = %{tl_version}, tex(vnss10.tfm) = %{tl_version}
Provides:       tex(vnss12.tfm) = %{tl_version}, tex(vnss17.tfm) = %{tl_version}
Provides:       tex(vnss8.tfm) = %{tl_version}, tex(vnss9.tfm) = %{tl_version}
Provides:       tex(vnssbx10.tfm) = %{tl_version}, tex(vnssdc10.tfm) = %{tl_version}
Provides:       tex(vnssi10.tfm) = %{tl_version}, tex(vnssi12.tfm) = %{tl_version}
Provides:       tex(vnssi17.tfm) = %{tl_version}, tex(vnssi8.tfm) = %{tl_version}
Provides:       tex(vnssi9.tfm) = %{tl_version}, tex(vnssq8.tfm) = %{tl_version}
Provides:       tex(vnssqi8.tfm) = %{tl_version}, tex(vntcsc10.tfm) = %{tl_version}
Provides:       tex(vnti10.tfm) = %{tl_version}, tex(vnti12.tfm) = %{tl_version}
Provides:       tex(vnti7.tfm) = %{tl_version}, tex(vnti8.tfm) = %{tl_version}
Provides:       tex(vnti9.tfm) = %{tl_version}, tex(vntt10.tfm) = %{tl_version}
Provides:       tex(vntt12.tfm) = %{tl_version}, tex(vntt8.tfm) = %{tl_version}
Provides:       tex(vntt9.tfm) = %{tl_version}, tex(vnu10.tfm) = %{tl_version}
Provides:       tex(vnvtt10.tfm) = %{tl_version}, tex(putb8v.tfm) = %{tl_version}
Provides:       tex(putbc8v.tfm) = %{tl_version}, tex(putbi8v.tfm) = %{tl_version}
Provides:       tex(putbo8v.tfm) = %{tl_version}, tex(putr8v.tfm) = %{tl_version}
Provides:       tex(putrc8v.tfm) = %{tl_version}, tex(putri8v.tfm) = %{tl_version}
Provides:       tex(putro8v.tfm) = %{tl_version}, tex(ArevSans-Bold-T5.pfb) = %{tl_version}
Provides:       tex(ArevSans-BoldOblique-T5.pfb) = %{tl_version}
Provides:       tex(ArevSans-Oblique-T5.pfb) = %{tl_version}
Provides:       tex(ArevSans-Roman-T5.pfb) = %{tl_version}
Provides:       tex(bchb8v.pfb) = %{tl_version}, tex(bchbi8v.pfb) = %{tl_version}
Provides:       tex(bchr8v.pfb) = %{tl_version}, tex(bchri8v.pfb) = %{tl_version}
Provides:       tex(vncmbr10.pfb) = %{tl_version}, tex(vncmbr17.pfb) = %{tl_version}
Provides:       tex(vncmbr8.pfb) = %{tl_version}, tex(vncmbr9.pfb) = %{tl_version}
Provides:       tex(vncmbrbx10.pfb) = %{tl_version}, tex(vncmbrsl10.pfb) = %{tl_version}
Provides:       tex(vncmbrsl17.pfb) = %{tl_version}, tex(vncmbrsl8.pfb) = %{tl_version}
Provides:       tex(vncmbrsl9.pfb) = %{tl_version}, tex(vncmsltl10.pfb) = %{tl_version}
Provides:       tex(vncmtl10.pfb) = %{tl_version}, tex(CMConcrete8v.pfb) = %{tl_version}
Provides:       tex(CMConcreteItalic8v.pfb) = %{tl_version}
Provides:       tex(CMConcreteSlanted8v.pfb) = %{tl_version}
Provides:       tex(CMConcreteSmallCaps8v.pfb) = %{tl_version}
Provides:       tex(ugqb8v.pfb) = %{tl_version}, tex(txbtt8v.pfb) = %{tl_version}
Provides:       tex(txbttsc8v.pfb) = %{tl_version}, tex(txtt8v.pfb) = %{tl_version}
Provides:       tex(txttsc8v.pfb) = %{tl_version}, tex(fplrc8v.pfb) = %{tl_version}
Provides:       tex(uagd8v.pfb) = %{tl_version}, tex(uagdo8v.pfb) = %{tl_version}
Provides:       tex(uagk8v.pfb) = %{tl_version}, tex(uagko8v.pfb) = %{tl_version}
Provides:       tex(ubkd8v.pfb) = %{tl_version}, tex(ubkdi8v.pfb) = %{tl_version}
Provides:       tex(ubkl8v.pfb) = %{tl_version}, tex(ubkli8v.pfb) = %{tl_version}
Provides:       tex(ucrb8v.pfb) = %{tl_version}, tex(ucrbo8v.pfb) = %{tl_version}
Provides:       tex(ucrr8v.pfb) = %{tl_version}, tex(ucrro8v.pfb) = %{tl_version}
Provides:       tex(uhvb8v.pfb) = %{tl_version}, tex(uhvbo8v.pfb) = %{tl_version}
Provides:       tex(uhvr8v.pfb) = %{tl_version}, tex(uhvro8v.pfb) = %{tl_version}
Provides:       tex(uncb8v.pfb) = %{tl_version}, tex(uncbi8v.pfb) = %{tl_version}
Provides:       tex(uncr8v.pfb) = %{tl_version}, tex(uncri8v.pfb) = %{tl_version}
Provides:       tex(uplb8v.pfb) = %{tl_version}, tex(uplbi8v.pfb) = %{tl_version}
Provides:       tex(uplr8v.pfb) = %{tl_version}, tex(uplri8v.pfb) = %{tl_version}
Provides:       tex(utmb8v.pfb) = %{tl_version}, tex(utmbi8v.pfb) = %{tl_version}
Provides:       tex(utmr8v.pfb) = %{tl_version}, tex(utmri8v.pfb) = %{tl_version}
Provides:       tex(uzcmi8v.pfb) = %{tl_version}, tex(vnb10.pfb) = %{tl_version}
Provides:       tex(vnbx10.pfb) = %{tl_version}, tex(vnbx12.pfb) = %{tl_version}
Provides:       tex(vnbx5.pfb) = %{tl_version}, tex(vnbx6.pfb) = %{tl_version}
Provides:       tex(vnbx7.pfb) = %{tl_version}, tex(vnbx8.pfb) = %{tl_version}
Provides:       tex(vnbx9.pfb) = %{tl_version}, tex(vnbxsl10.pfb) = %{tl_version}
Provides:       tex(vnbxti10.pfb) = %{tl_version}, tex(vncsc10.pfb) = %{tl_version}
Provides:       tex(vndunh10.pfb) = %{tl_version}, tex(vnff10.pfb) = %{tl_version}
Provides:       tex(vnfi10.pfb) = %{tl_version}, tex(vnfib8.pfb) = %{tl_version}
Provides:       tex(vnitt10.pfb) = %{tl_version}, tex(vnr10.pfb) = %{tl_version}
Provides:       tex(vnr12.pfb) = %{tl_version}, tex(vnr17.pfb) = %{tl_version}
Provides:       tex(vnr5.pfb) = %{tl_version}, tex(vnr6.pfb) = %{tl_version}
Provides:       tex(vnr7.pfb) = %{tl_version}, tex(vnr8.pfb) = %{tl_version}
Provides:       tex(vnr9.pfb) = %{tl_version}, tex(vnsl10.pfb) = %{tl_version}
Provides:       tex(vnsl12.pfb) = %{tl_version}, tex(vnsl8.pfb) = %{tl_version}
Provides:       tex(vnsl9.pfb) = %{tl_version}, tex(vnsltt10.pfb) = %{tl_version}
Provides:       tex(vnss10.pfb) = %{tl_version}, tex(vnss12.pfb) = %{tl_version}
Provides:       tex(vnss17.pfb) = %{tl_version}, tex(vnss8.pfb) = %{tl_version}
Provides:       tex(vnss9.pfb) = %{tl_version}, tex(vnssbx10.pfb) = %{tl_version}
Provides:       tex(vnssdc10.pfb) = %{tl_version}, tex(vnssi10.pfb) = %{tl_version}
Provides:       tex(vnssi12.pfb) = %{tl_version}, tex(vnssi17.pfb) = %{tl_version}
Provides:       tex(vnssi8.pfb) = %{tl_version}, tex(vnssi9.pfb) = %{tl_version}
Provides:       tex(vnssq8.pfb) = %{tl_version}, tex(vnssqi8.pfb) = %{tl_version}
Provides:       tex(vntcsc10.pfb) = %{tl_version}, tex(vnti10.pfb) = %{tl_version}
Provides:       tex(vnti12.pfb) = %{tl_version}, tex(vnti7.pfb) = %{tl_version}
Provides:       tex(vnti8.pfb) = %{tl_version}, tex(vnti9.pfb) = %{tl_version}
Provides:       tex(vntt10.pfb) = %{tl_version}, tex(vntt12.pfb) = %{tl_version}
Provides:       tex(vntt8.pfb) = %{tl_version}, tex(vntt9.pfb) = %{tl_version}
Provides:       tex(vnu10.pfb) = %{tl_version}, tex(vnvtt10.pfb) = %{tl_version}
Provides:       tex(putb8v.pfb) = %{tl_version}, tex(putbi8v.pfb) = %{tl_version}
Provides:       tex(putr8v.pfb) = %{tl_version}, tex(putri8v.pfb) = %{tl_version}
Provides:       tex(bchbc8v.vf) = %{tl_version}, tex(bchrc8v.vf) = %{tl_version}
Provides:       tex(uagdc8v.vf) = %{tl_version}, tex(uagkc8v.vf) = %{tl_version}
Provides:       tex(ubkdc8v.vf) = %{tl_version}, tex(ubklc8v.vf) = %{tl_version}
Provides:       tex(ucrbc8v.vf) = %{tl_version}, tex(ucrrc8v.vf) = %{tl_version}
Provides:       tex(uhvbc8v.vf) = %{tl_version}, tex(uhvrc8v.vf) = %{tl_version}
Provides:       tex(uncbc8v.vf) = %{tl_version}, tex(uncrc8v.vf) = %{tl_version}
Provides:       tex(uplbc8v.vf) = %{tl_version}, tex(uplrc8v.vf) = %{tl_version}
Provides:       tex(utmbc8v.vf) = %{tl_version}, tex(utmrc8v.vf) = %{tl_version}
Provides:       tex(putbc8v.vf) = %{tl_version}, tex(putrc8v.vf) = %{tl_version}
Provides:       tex(dblaccnt.sty) = %{tl_version}, tex(mcviscii.def) = %{tl_version}
Provides:       tex(pd1supp.def) = %{tl_version}, tex(swpvntex.sty) = %{tl_version}
Provides:       tex(t5bch.fd) = %{tl_version}, tex(t5ccr.fd) = %{tl_version}
Provides:       tex(t5cmbr.fd) = %{tl_version}, tex(t5cmdh.fd) = %{tl_version}
Provides:       tex(t5cmfib.fd) = %{tl_version}, tex(t5cmfr.fd) = %{tl_version}
Provides:       tex(t5cmr.fd) = %{tl_version}, tex(t5cmss.fd) = %{tl_version}
Provides:       tex(t5cmssq.fd) = %{tl_version}, tex(t5cmtl.fd) = %{tl_version}
Provides:       tex(t5cmtt.fd) = %{tl_version}, tex(t5cmvtt.fd) = %{tl_version}
Provides:       tex(t5enc.def) = %{tl_version}, tex(t5fav.fd) = %{tl_version}
Provides:       tex(t5fnc.fd) = %{tl_version}, tex(t5fpl.fd) = %{tl_version}
Provides:       tex(t5futs.fd) = %{tl_version}, tex(t5mak.fd) = %{tl_version}
Provides:       tex(t5mdbch.fd) = %{tl_version}, tex(t5mdput.fd) = %{tl_version}
Provides:       tex(t5mdugm.fd) = %{tl_version}, tex(t5pag.fd) = %{tl_version}
Provides:       tex(t5pbk.fd) = %{tl_version}, tex(t5pcr.fd) = %{tl_version}
Provides:       tex(t5phv.fd) = %{tl_version}, tex(t5pnc.fd) = %{tl_version}
Provides:       tex(t5ppl.fd) = %{tl_version}, tex(t5ptm.fd) = %{tl_version}
Provides:       tex(t5ptmom.fd) = %{tl_version}, tex(t5put.fd) = %{tl_version}
Provides:       tex(t5pxr.fd) = %{tl_version}, tex(t5txr.fd) = %{tl_version}
Provides:       tex(t5txtt.fd) = %{tl_version}, tex(t5uag.fd) = %{tl_version}
Provides:       tex(t5ubk.fd) = %{tl_version}, tex(t5ucr.fd) = %{tl_version}
Provides:       tex(t5ugq.fd) = %{tl_version}, tex(t5uhv.fd) = %{tl_version}
Provides:       tex(t5unc.fd) = %{tl_version}, tex(t5upl.fd) = %{tl_version}
Provides:       tex(t5utm.fd) = %{tl_version}, tex(t5uzcm.fd) = %{tl_version}
Provides:       tex(tcvn.def) = %{tl_version}, tex(varioref-vi.sty) = %{tl_version}
Provides:       tex(vietnam.sty) = %{tl_version}, tex(viscii.def) = %{tl_version}
Provides:       tex(vncaps.tex) = %{tl_version}, tex(vntex.sty) = %{tl_version}
Provides:       tex(vps.def) = %{tl_version}, tex(dblaccnt.tex) = %{tl_version}
Provides:       tex(t5code.tex) = %{tl_version}, tex(vntexinfo.tex) = %{tl_version}

%description -n texlive-vntex
The vntex bundle provides fonts, Plain TeX, texinfo and LaTeX
macros for typesetting documents in Vietnamese. Users of the
fonts (in both Metafont and Adobe Type 1 format) of this bundle
may alternatively use the lm fonts bundle, for which map files
are available to provide a Vietnamese version.

%package -n texlive-vntex-doc
Summary:        Documentation for vntex
Version:        svn30579.3.2

Provides:       tex-vntex-doc
AutoReqProv:    No

%description -n texlive-vntex-doc
Documentation for vntex

%package -n texlive-uml
Provides:       tex-uml = %{tl_version}
License:        LPPL
Summary:        UML diagrams in LaTeX
Version:        svn17476.0.11

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty), tex(pst-node.sty), tex(pst-xkey.sty), tex(relsize.sty)
Provides:       tex(uml.sty) = %{tl_version}

%description -n texlive-uml
A PSTricks related package for writing UML (Unified Modelling
Language) diagrams in LaTeX. Currently, it implements a subset
of class diagrams, and some extra constructs as well. The
package cannot be used together with pst-uml.

%package -n texlive-uml-doc
Summary:        Documentation for uml
Version:        svn17476.0.11

Provides:       tex-uml-doc
AutoReqProv:    No

%description -n texlive-uml-doc
Documentation for uml

%package -n texlive-umlaute
Provides:       tex-umlaute = %{tl_version}
License:        LPPL
Summary:        German input encodings in LaTeX
Version:        svn15878.v2.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(inputenc.sty)
Provides:       tex(atari.def) = %{tl_version}, tex(isolatin.def) = %{tl_version}
Provides:       tex(mac.def) = %{tl_version}, tex(pc850.def) = %{tl_version}
Provides:       tex(roman8.def) = %{tl_version}, tex(umlaute.sty) = %{tl_version}

%description -n texlive-umlaute
An early package for using alternate input encodings. The
author considers the package mostly obsolete, since most of its
functions are taken by the inputenc package; however, inputenc
doesn't support the roman8 and atari encodings, so umlaute
remains the sole source of that support.

%package -n texlive-umlaute-doc
Summary:        Documentation for umlaute
Version:        svn15878.v2.1

Provides:       tex-umlaute-doc
AutoReqProv:    No

%description -n texlive-umlaute-doc
Documentation for umlaute

%package -n texlive-umtypewriter
Provides:       tex-umtypewriter = %{tl_version}
License:        OFL
Summary:        Fonts to typeset with the xgreek package
Version:        svn18651.001.002

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(UMTypewriter-Bold.otf) = %{tl_version}
Provides:       tex(UMTypewriter-BoldItalic.otf) = %{tl_version}
Provides:       tex(UMTypewriter-Italic.otf) = %{tl_version}
Provides:       tex(UMTypewriter-Oblique.otf) = %{tl_version}
Provides:       tex(UMTypewriter-Regular.otf) = %{tl_version}

%description -n texlive-umtypewriter
The UMTypewriter font family is a monospaced font family that
was built from glyphs from the CB Greek fonts, the CyrTUG
Cyrillic alphabet fonts ("LH"), and the standard Computer
Modern font family. It contains four OpenType fonts which are
required for use of the xgreek package for XeLaTeX.

%package -n texlive-universa
Provides:       tex-universa = %{tl_version}
License:        GPL+
Summary:        Herbert Bayer's 'universal' font
Version:        svn15878.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(fulbc10.tfm) = %{tl_version}, tex(fulbc12.tfm) = %{tl_version}
Provides:       tex(fulbc17.tfm) = %{tl_version}, tex(fulbc8.tfm) = %{tl_version}
Provides:       tex(fulbc9.tfm) = %{tl_version}, tex(fulbo10.tfm) = %{tl_version}
Provides:       tex(fulbo12.tfm) = %{tl_version}, tex(fulbo17.tfm) = %{tl_version}
Provides:       tex(fulbo8.tfm) = %{tl_version}, tex(fulbo9.tfm) = %{tl_version}
Provides:       tex(fulbr10.tfm) = %{tl_version}, tex(fulbr12.tfm) = %{tl_version}
Provides:       tex(fulbr17.tfm) = %{tl_version}, tex(fulbr8.tfm) = %{tl_version}
Provides:       tex(fulbr9.tfm) = %{tl_version}, tex(fulbst10.tfm) = %{tl_version}
Provides:       tex(fulbst12.tfm) = %{tl_version}, tex(fulbst17.tfm) = %{tl_version}
Provides:       tex(fulbst8.tfm) = %{tl_version}, tex(fulbst9.tfm) = %{tl_version}
Provides:       tex(fulmc10.tfm) = %{tl_version}, tex(fulmc12.tfm) = %{tl_version}
Provides:       tex(fulmc17.tfm) = %{tl_version}, tex(fulmc8.tfm) = %{tl_version}
Provides:       tex(fulmc9.tfm) = %{tl_version}, tex(fulmo10.tfm) = %{tl_version}
Provides:       tex(fulmo12.tfm) = %{tl_version}, tex(fulmo17.tfm) = %{tl_version}
Provides:       tex(fulmo8.tfm) = %{tl_version}, tex(fulmo9.tfm) = %{tl_version}
Provides:       tex(fulmr10.tfm) = %{tl_version}, tex(fulmr12.tfm) = %{tl_version}
Provides:       tex(fulmr17.tfm) = %{tl_version}, tex(fulmr8.tfm) = %{tl_version}
Provides:       tex(fulmr9.tfm) = %{tl_version}, tex(fulmst10.tfm) = %{tl_version}
Provides:       tex(fulmst12.tfm) = %{tl_version}, tex(fulmst17.tfm) = %{tl_version}
Provides:       tex(fulmst8.tfm) = %{tl_version}, tex(fulmst9.tfm) = %{tl_version}
Provides:       tex(omluni.fd) = %{tl_version}, tex(omsuni.fd) = %{tl_version}
Provides:       tex(ot1uni.fd) = %{tl_version}, tex(t1uni.fd) = %{tl_version}
Provides:       tex(uni.sty) = %{tl_version}, tex(uuni.fd) = %{tl_version}

%description -n texlive-universa
An implementation of the universal font by Herbert Bayer of the
Bauhaus school. The Metafont sources of the fonts, and their
LaTeX support, are all supplied in a LaTeX documented source
(.dtx) file.

%package -n texlive-universa-doc
Summary:        Documentation for universa
Version:        svn15878.2.0

Provides:       tex-universa-doc
AutoReqProv:    No

%description -n texlive-universa-doc
Documentation for universa

%package -n texlive-universalis
Provides:       tex-universalis = %{tl_version}
License:        GPLv2+
Summary:        Universalis font, with support
Version:        svn33860.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(fontenc.sty), tex(textcomp.sty), tex(mweights.sty), tex(fontaxes.sty)
Requires:       tex(xkeyval.sty), tex(ifxetex.sty), tex(ifluatex.sty), tex(fontspec.sty)
Provides:       tex(unvsl_fe7xck.enc) = %{tl_version}, tex(unvsl_qu6a6x.enc) = %{tl_version}
Provides:       tex(unvsl_sjpjw4.enc) = %{tl_version}, tex(unvsl_xtabpf.enc) = %{tl_version}
Provides:       tex(universalis.map) = %{tl_version}, tex(UniversalisADFStd-Bold.otf) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCond.otf) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCondIt.otf) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldItalic.otf) = %{tl_version}
Provides:       tex(UniversalisADFStd-Cond.otf) = %{tl_version}
Provides:       tex(UniversalisADFStd-CondItalic.otf) = %{tl_version}
Provides:       tex(UniversalisADFStd-Italic.otf) = %{tl_version}
Provides:       tex(UniversalisADFStd-Regular.otf) = %{tl_version}
Provides:       tex(UniversalisADFStd-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Bold-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Bold-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Bold-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Bold-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCond-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCond-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCond-lf-ly1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCond-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCond-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCond-lf-ot1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCond-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCond-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCond-lf-t1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCond-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCond-lf-ts1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCondIt-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCondIt-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCondIt-lf-ly1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCondIt-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCondIt-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCondIt-lf-ot1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCondIt-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCondIt-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCondIt-lf-t1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCondIt-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCondIt-lf-ts1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldItalic-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldItalic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldItalic-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldItalic-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Cond-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Cond-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Cond-lf-ly1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Cond-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Cond-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Cond-lf-ot1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Cond-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Cond-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Cond-lf-t1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Cond-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Cond-lf-ts1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-CondItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-CondItalic-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-CondItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-CondItalic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-CondItalic-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-CondItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-CondItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-CondItalic-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-CondItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-CondItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-CondItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Italic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Italic-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Italic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Italic-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Italic-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Regular-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Regular-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Regular-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Regular-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(UniversalisADFStd-Bold.pfb) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCond.pfb) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCondIt.pfb) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCondItLCDFJ.pfb) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCondLCDFJ.pfb) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldItalic.pfb) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldItalicLCDFJ.pfb) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldLCDFJ.pfb) = %{tl_version}
Provides:       tex(UniversalisADFStd-Cond.pfb) = %{tl_version}
Provides:       tex(UniversalisADFStd-CondItalic.pfb) = %{tl_version}
Provides:       tex(UniversalisADFStd-CondItalicLCDFJ.pfb) = %{tl_version}
Provides:       tex(UniversalisADFStd-CondLCDFJ.pfb) = %{tl_version}
Provides:       tex(UniversalisADFStd-Italic.pfb) = %{tl_version}
Provides:       tex(UniversalisADFStd-ItalicLCDFJ.pfb) = %{tl_version}
Provides:       tex(UniversalisADFStd-Regular.pfb) = %{tl_version}
Provides:       tex(UniversalisADFStd-RegularLCDFJ.pfb) = %{tl_version}
Provides:       tex(UniversalisADFStd-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-Bold-lf-ot1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCond-lf-ly1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCond-lf-ot1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCond-lf-t1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCond-lf-ts1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCondIt-lf-ly1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCondIt-lf-ot1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCondIt-lf-t1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldCondIt-lf-ts1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldItalic-lf-ot1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-Cond-lf-ly1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-Cond-lf-ot1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-Cond-lf-t1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-Cond-lf-ts1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-CondItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-CondItalic-lf-ot1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-CondItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-CondItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-Italic-lf-ly1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-Italic-lf-ot1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-Regular-lf-ot1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(UniversalisADFStd-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(LY1UniversalisADFStd-LF.fd) = %{tl_version}
Provides:       tex(OT1UniversalisADFStd-LF.fd) = %{tl_version}
Provides:       tex(T1UniversalisADFStd-LF.fd) = %{tl_version}
Provides:       tex(TS1UniversalisADFStd-LF.fd) = %{tl_version}
Provides:       tex(UniversalisADFStd.sty) = %{tl_version}
Provides:       tex(universalis.sty) = %{tl_version}

%description -n texlive-universalis
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the UniversalisADFStd family of fonts, designed by
Hirwin Harendal. The font is suitable as an alternative to
fonts such as Adrian Frutiger's Univers and Frutiger.

%package -n texlive-universalis-doc
Summary:        Documentation for universalis
Version:        svn33860.0

Provides:       tex-universalis-doc
AutoReqProv:    No

%description -n texlive-universalis-doc
Documentation for universalis

%package -n texlive-urwchancal
Provides:       tex-urwchancal = %{tl_version}
License:        LPPL
Summary:        Use URW's clone of Zapf Chancery as a maths alphabet
Version:        svn21701.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty)
Provides:       tex(urwchancal.tfm) = %{tl_version}, tex(urwchancal.vf) = %{tl_version}
Provides:       tex(urwchancal.sty) = %{tl_version}, tex(uurwchancal.fd) = %{tl_version}

%description -n texlive-urwchancal
The package allows (the URW clone of) Zapf Chancery to function
as a maths alphabet, the target of \mathcal or \mathscr, with
accents appearing where they should, and other spacing
parameters set to reasonable (not very tight) values. The font
itself may be found in the URW basic fonts collection. This
package supersedes the pzccal package.

%package -n texlive-urwchancal-doc
Summary:        Documentation for urwchancal
Version:        svn21701.1

Provides:       tex-urwchancal-doc
AutoReqProv:    No

%description -n texlive-urwchancal-doc
Documentation for urwchancal

%package -n texlive-venturisadf
Provides:       tex-venturisadf = %{tl_version}
License:        Utopia
Summary:        Venturis ADF fonts collection
Version:        svn19444.1.005

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(xkeyval.sty), tex(fontenc.sty), tex(textcomp.sty), tex(nfssext-cfr.sty)
Provides:       tex(t1-dotalt-f_f-venturisadf.enc) = %{tl_version}
Provides:       tex(t1-f_f-venturisadf.enc) = %{tl_version}
Provides:       tex(t1-venturis.enc) = %{tl_version}, tex(t1-venturisold-longs.enc) = %{tl_version}
Provides:       tex(ts1-euro-venturisadf.enc) = %{tl_version}
Provides:       tex(yvt.map) = %{tl_version}, tex(yv2.map) = %{tl_version}
Provides:       tex(yvo.map) = %{tl_version}, tex(yv1.map) = %{tl_version}
Provides:       tex(yv3.map) = %{tl_version}, tex(t1-yvtb-c.tfm) = %{tl_version}
Provides:       tex(t1-yvtb.tfm) = %{tl_version}, tex(t1-yvtbc-c.tfm) = %{tl_version}
Provides:       tex(t1-yvtbc.tfm) = %{tl_version}, tex(t1-yvtbci-c.tfm) = %{tl_version}
Provides:       tex(t1-yvtbci.tfm) = %{tl_version}, tex(t1-yvtbd-c.tfm) = %{tl_version}
Provides:       tex(t1-yvtbi-c.tfm) = %{tl_version}, tex(t1-yvtbi.tfm) = %{tl_version}
Provides:       tex(t1-yvth.tfm) = %{tl_version}, tex(t1-yvthi.tfm) = %{tl_version}
Provides:       tex(t1-yvtr-c.tfm) = %{tl_version}, tex(t1-yvtr.tfm) = %{tl_version}
Provides:       tex(t1-yvtrc-c.tfm) = %{tl_version}, tex(t1-yvtrc.tfm) = %{tl_version}
Provides:       tex(t1-yvtrci-c.tfm) = %{tl_version}, tex(t1-yvtrci.tfm) = %{tl_version}
Provides:       tex(t1-yvtrdl.tfm) = %{tl_version}, tex(t1-yvtri-c.tfm) = %{tl_version}
Provides:       tex(t1-yvtri.tfm) = %{tl_version}, tex(t1alt-yvtbc-c.tfm) = %{tl_version}
Provides:       tex(t1alt-yvtbc.tfm) = %{tl_version}, tex(t1alt-yvtbci-c.tfm) = %{tl_version}
Provides:       tex(t1alt-yvtbci.tfm) = %{tl_version}, tex(t1alt-yvtrc-c.tfm) = %{tl_version}
Provides:       tex(t1alt-yvtrc.tfm) = %{tl_version}, tex(t1alt-yvtrci-c.tfm) = %{tl_version}
Provides:       tex(t1alt-yvtrci.tfm) = %{tl_version}, tex(ts1-yvtb-c.tfm) = %{tl_version}
Provides:       tex(ts1-yvtb.tfm) = %{tl_version}, tex(ts1-yvtbc-c.tfm) = %{tl_version}
Provides:       tex(ts1-yvtbc.tfm) = %{tl_version}, tex(ts1-yvtbci-c.tfm) = %{tl_version}
Provides:       tex(ts1-yvtbci.tfm) = %{tl_version}, tex(ts1-yvtbd-c.tfm) = %{tl_version}
Provides:       tex(ts1-yvtbi-c.tfm) = %{tl_version}, tex(ts1-yvtbi.tfm) = %{tl_version}
Provides:       tex(ts1-yvth.tfm) = %{tl_version}, tex(ts1-yvthi.tfm) = %{tl_version}
Provides:       tex(ts1-yvtr-c.tfm) = %{tl_version}, tex(ts1-yvtr.tfm) = %{tl_version}
Provides:       tex(ts1-yvtrc-c.tfm) = %{tl_version}, tex(ts1-yvtrc.tfm) = %{tl_version}
Provides:       tex(ts1-yvtrci-c.tfm) = %{tl_version}, tex(ts1-yvtrci.tfm) = %{tl_version}
Provides:       tex(ts1-yvtrdl.tfm) = %{tl_version}, tex(ts1-yvtri-c.tfm) = %{tl_version}
Provides:       tex(ts1-yvtri.tfm) = %{tl_version}, tex(vent-yvtr.tfm) = %{tl_version}
Provides:       tex(yvtb8c.tfm) = %{tl_version}, tex(yvtb8cc.tfm) = %{tl_version}
Provides:       tex(yvtb8t.tfm) = %{tl_version}, tex(yvtb8tc.tfm) = %{tl_version}
Provides:       tex(yvtbc8c.tfm) = %{tl_version}, tex(yvtbc8cc.tfm) = %{tl_version}
Provides:       tex(yvtbc8t.tfm) = %{tl_version}, tex(yvtbc8tc.tfm) = %{tl_version}
Provides:       tex(yvtbci8c.tfm) = %{tl_version}, tex(yvtbci8cc.tfm) = %{tl_version}
Provides:       tex(yvtbci8t.tfm) = %{tl_version}, tex(yvtbci8tc.tfm) = %{tl_version}
Provides:       tex(yvtbcij8t.tfm) = %{tl_version}, tex(yvtbcij8tc.tfm) = %{tl_version}
Provides:       tex(yvtbcijw8t.tfm) = %{tl_version}, tex(yvtbcijw8tc.tfm) = %{tl_version}
Provides:       tex(yvtbciw8t.tfm) = %{tl_version}, tex(yvtbciw8tc.tfm) = %{tl_version}
Provides:       tex(yvtbcj8t.tfm) = %{tl_version}, tex(yvtbcj8tc.tfm) = %{tl_version}
Provides:       tex(yvtbcjw8t.tfm) = %{tl_version}, tex(yvtbcjw8tc.tfm) = %{tl_version}
Provides:       tex(yvtbcw8t.tfm) = %{tl_version}, tex(yvtbcw8tc.tfm) = %{tl_version}
Provides:       tex(yvtbd8cc.tfm) = %{tl_version}, tex(yvtbd8tc.tfm) = %{tl_version}
Provides:       tex(yvtbi8c.tfm) = %{tl_version}, tex(yvtbi8cc.tfm) = %{tl_version}
Provides:       tex(yvtbi8t.tfm) = %{tl_version}, tex(yvtbi8tc.tfm) = %{tl_version}
Provides:       tex(yvtbij8t.tfm) = %{tl_version}, tex(yvtbij8tc.tfm) = %{tl_version}
Provides:       tex(yvtbijw8t.tfm) = %{tl_version}, tex(yvtbijw8tc.tfm) = %{tl_version}
Provides:       tex(yvtbiw8t.tfm) = %{tl_version}, tex(yvtbiw8tc.tfm) = %{tl_version}
Provides:       tex(yvtbj8t.tfm) = %{tl_version}, tex(yvtbj8tc.tfm) = %{tl_version}
Provides:       tex(yvtbjw8t.tfm) = %{tl_version}, tex(yvtbjw8tc.tfm) = %{tl_version}
Provides:       tex(yvtbw8t.tfm) = %{tl_version}, tex(yvtbw8tc.tfm) = %{tl_version}
Provides:       tex(yvth8c.tfm) = %{tl_version}, tex(yvth8t.tfm) = %{tl_version}
Provides:       tex(yvthi8c.tfm) = %{tl_version}, tex(yvthi8t.tfm) = %{tl_version}
Provides:       tex(yvtr8c.tfm) = %{tl_version}, tex(yvtr8cc.tfm) = %{tl_version}
Provides:       tex(yvtr8t.tfm) = %{tl_version}, tex(yvtr8tc.tfm) = %{tl_version}
Provides:       tex(yvtrajw8t.tfm) = %{tl_version}, tex(yvtraw8t.tfm) = %{tl_version}
Provides:       tex(yvtrc8c.tfm) = %{tl_version}, tex(yvtrc8cc.tfm) = %{tl_version}
Provides:       tex(yvtrc8t.tfm) = %{tl_version}, tex(yvtrc8tc.tfm) = %{tl_version}
Provides:       tex(yvtrci8c.tfm) = %{tl_version}, tex(yvtrci8cc.tfm) = %{tl_version}
Provides:       tex(yvtrci8t.tfm) = %{tl_version}, tex(yvtrci8tc.tfm) = %{tl_version}
Provides:       tex(yvtrcij8t.tfm) = %{tl_version}, tex(yvtrcij8tc.tfm) = %{tl_version}
Provides:       tex(yvtrcijw8t.tfm) = %{tl_version}, tex(yvtrcijw8tc.tfm) = %{tl_version}
Provides:       tex(yvtrciw8t.tfm) = %{tl_version}, tex(yvtrciw8tc.tfm) = %{tl_version}
Provides:       tex(yvtrcj8t.tfm) = %{tl_version}, tex(yvtrcj8tc.tfm) = %{tl_version}
Provides:       tex(yvtrcjw8t.tfm) = %{tl_version}, tex(yvtrcjw8tc.tfm) = %{tl_version}
Provides:       tex(yvtrcw8t.tfm) = %{tl_version}, tex(yvtrcw8tc.tfm) = %{tl_version}
Provides:       tex(yvtrdl8c.tfm) = %{tl_version}, tex(yvtrdl8t.tfm) = %{tl_version}
Provides:       tex(yvtri8c.tfm) = %{tl_version}, tex(yvtri8cc.tfm) = %{tl_version}
Provides:       tex(yvtri8t.tfm) = %{tl_version}, tex(yvtri8tc.tfm) = %{tl_version}
Provides:       tex(yvtrij8t.tfm) = %{tl_version}, tex(yvtrij8tc.tfm) = %{tl_version}
Provides:       tex(yvtrijw8t.tfm) = %{tl_version}, tex(yvtrijw8tc.tfm) = %{tl_version}
Provides:       tex(yvtriw8t.tfm) = %{tl_version}, tex(yvtriw8tc.tfm) = %{tl_version}
Provides:       tex(yvtrj8t.tfm) = %{tl_version}, tex(yvtrj8tc.tfm) = %{tl_version}
Provides:       tex(yvtrjw8t.tfm) = %{tl_version}, tex(yvtrjw8tc.tfm) = %{tl_version}
Provides:       tex(yvtrw8t.tfm) = %{tl_version}, tex(yvtrw8tc.tfm) = %{tl_version}
Provides:       tex(t1-yv2b-c.tfm) = %{tl_version}, tex(t1-yv2b.tfm) = %{tl_version}
Provides:       tex(t1-yv2bi-c.tfm) = %{tl_version}, tex(t1-yv2bi.tfm) = %{tl_version}
Provides:       tex(t1-yv2m.tfm) = %{tl_version}, tex(t1-yv2mi.tfm) = %{tl_version}
Provides:       tex(t1-yv2r-c.tfm) = %{tl_version}, tex(t1-yv2r.tfm) = %{tl_version}
Provides:       tex(t1-yv2ri-c.tfm) = %{tl_version}, tex(t1-yv2ri.tfm) = %{tl_version}
Provides:       tex(t1-yv2x.tfm) = %{tl_version}, tex(t1-yv2xi.tfm) = %{tl_version}
Provides:       tex(ts1-yv2b-c.tfm) = %{tl_version}, tex(ts1-yv2b.tfm) = %{tl_version}
Provides:       tex(ts1-yv2bi-c.tfm) = %{tl_version}, tex(ts1-yv2bi.tfm) = %{tl_version}
Provides:       tex(ts1-yv2m.tfm) = %{tl_version}, tex(ts1-yv2mi.tfm) = %{tl_version}
Provides:       tex(ts1-yv2r-c.tfm) = %{tl_version}, tex(ts1-yv2r.tfm) = %{tl_version}
Provides:       tex(ts1-yv2ri-c.tfm) = %{tl_version}, tex(ts1-yv2ri.tfm) = %{tl_version}
Provides:       tex(ts1-yv2x.tfm) = %{tl_version}, tex(ts1-yv2xi.tfm) = %{tl_version}
Provides:       tex(yv2b8c.tfm) = %{tl_version}, tex(yv2b8cc.tfm) = %{tl_version}
Provides:       tex(yv2b8t.tfm) = %{tl_version}, tex(yv2b8tc.tfm) = %{tl_version}
Provides:       tex(yv2bi8c.tfm) = %{tl_version}, tex(yv2bi8cc.tfm) = %{tl_version}
Provides:       tex(yv2bi8t.tfm) = %{tl_version}, tex(yv2bi8tc.tfm) = %{tl_version}
Provides:       tex(yv2m8c.tfm) = %{tl_version}, tex(yv2m8t.tfm) = %{tl_version}
Provides:       tex(yv2mi8c.tfm) = %{tl_version}, tex(yv2mi8t.tfm) = %{tl_version}
Provides:       tex(yv2r8c.tfm) = %{tl_version}, tex(yv2r8cc.tfm) = %{tl_version}
Provides:       tex(yv2r8t.tfm) = %{tl_version}, tex(yv2r8tc.tfm) = %{tl_version}
Provides:       tex(yv2ri8c.tfm) = %{tl_version}, tex(yv2ri8cc.tfm) = %{tl_version}
Provides:       tex(yv2ri8t.tfm) = %{tl_version}, tex(yv2ri8tc.tfm) = %{tl_version}
Provides:       tex(yv2x8c.tfm) = %{tl_version}, tex(yv2x8t.tfm) = %{tl_version}
Provides:       tex(yv2xi8c.tfm) = %{tl_version}, tex(yv2xi8t.tfm) = %{tl_version}
Provides:       tex(t1-yvob.tfm) = %{tl_version}, tex(t1-yvobi.tfm) = %{tl_version}
Provides:       tex(t1-yvodd.tfm) = %{tl_version}, tex(t1-yvor.tfm) = %{tl_version}
Provides:       tex(t1-yvori.tfm) = %{tl_version}, tex(ts1-yvob.tfm) = %{tl_version}
Provides:       tex(ts1-yvobi.tfm) = %{tl_version}, tex(ts1-yvodd.tfm) = %{tl_version}
Provides:       tex(ts1-yvor.tfm) = %{tl_version}, tex(ts1-yvori.tfm) = %{tl_version}
Provides:       tex(yvoab8t.tfm) = %{tl_version}, tex(yvoabi8t.tfm) = %{tl_version}
Provides:       tex(yvoar8t.tfm) = %{tl_version}, tex(yvoari8t.tfm) = %{tl_version}
Provides:       tex(yvob8c.tfm) = %{tl_version}, tex(yvob8t.tfm) = %{tl_version}
Provides:       tex(yvobi8c.tfm) = %{tl_version}, tex(yvobi8t.tfm) = %{tl_version}
Provides:       tex(yvodd8c.tfm) = %{tl_version}, tex(yvodd8t.tfm) = %{tl_version}
Provides:       tex(yvor8c.tfm) = %{tl_version}, tex(yvor8t.tfm) = %{tl_version}
Provides:       tex(yvori8c.tfm) = %{tl_version}, tex(yvori8t.tfm) = %{tl_version}
Provides:       tex(t1-yv1b-c.tfm) = %{tl_version}, tex(t1-yv1b-x.tfm) = %{tl_version}
Provides:       tex(t1-yv1b.tfm) = %{tl_version}, tex(t1-yv1bd.tfm) = %{tl_version}
Provides:       tex(t1-yv1bi-c.tfm) = %{tl_version}, tex(t1-yv1bi-x.tfm) = %{tl_version}
Provides:       tex(t1-yv1bi.tfm) = %{tl_version}, tex(t1-yv1d.tfm) = %{tl_version}
Provides:       tex(t1-yv1dd-u.tfm) = %{tl_version}, tex(t1-yv1di.tfm) = %{tl_version}
Provides:       tex(t1-yv1h.tfm) = %{tl_version}, tex(t1-yv1ho.tfm) = %{tl_version}
Provides:       tex(t1-yv1l.tfm) = %{tl_version}, tex(t1-yv1li.tfm) = %{tl_version}
Provides:       tex(t1-yv1r-c.tfm) = %{tl_version}, tex(t1-yv1r-x.tfm) = %{tl_version}
Provides:       tex(t1-yv1r.tfm) = %{tl_version}, tex(t1-yv1ri-c.tfm) = %{tl_version}
Provides:       tex(t1-yv1ri-x.tfm) = %{tl_version}, tex(t1-yv1ri.tfm) = %{tl_version}
Provides:       tex(ts1-yv1b-c.tfm) = %{tl_version}, tex(ts1-yv1b-x.tfm) = %{tl_version}
Provides:       tex(ts1-yv1b.tfm) = %{tl_version}, tex(ts1-yv1bd.tfm) = %{tl_version}
Provides:       tex(ts1-yv1bi-c.tfm) = %{tl_version}, tex(ts1-yv1bi-x.tfm) = %{tl_version}
Provides:       tex(ts1-yv1bi.tfm) = %{tl_version}, tex(ts1-yv1d.tfm) = %{tl_version}
Provides:       tex(ts1-yv1dd-u.tfm) = %{tl_version}, tex(ts1-yv1di.tfm) = %{tl_version}
Provides:       tex(ts1-yv1h.tfm) = %{tl_version}, tex(ts1-yv1ho.tfm) = %{tl_version}
Provides:       tex(ts1-yv1l.tfm) = %{tl_version}, tex(ts1-yv1li.tfm) = %{tl_version}
Provides:       tex(ts1-yv1r-c.tfm) = %{tl_version}, tex(ts1-yv1r-x.tfm) = %{tl_version}
Provides:       tex(ts1-yv1r.tfm) = %{tl_version}, tex(ts1-yv1ri-c.tfm) = %{tl_version}
Provides:       tex(ts1-yv1ri-x.tfm) = %{tl_version}, tex(ts1-yv1ri.tfm) = %{tl_version}
Provides:       tex(yv1b8c.tfm) = %{tl_version}, tex(yv1b8cc.tfm) = %{tl_version}
Provides:       tex(yv1b8cx.tfm) = %{tl_version}, tex(yv1b8t.tfm) = %{tl_version}
Provides:       tex(yv1b8tc.tfm) = %{tl_version}, tex(yv1b8tx.tfm) = %{tl_version}
Provides:       tex(yv1bd8c.tfm) = %{tl_version}, tex(yv1bd8t.tfm) = %{tl_version}
Provides:       tex(yv1bi8c.tfm) = %{tl_version}, tex(yv1bi8cc.tfm) = %{tl_version}
Provides:       tex(yv1bi8cx.tfm) = %{tl_version}, tex(yv1bi8t.tfm) = %{tl_version}
Provides:       tex(yv1bi8tc.tfm) = %{tl_version}, tex(yv1bi8tx.tfm) = %{tl_version}
Provides:       tex(yv1d8c.tfm) = %{tl_version}, tex(yv1d8t.tfm) = %{tl_version}
Provides:       tex(yv1dd8cu.tfm) = %{tl_version}, tex(yv1dd8tu.tfm) = %{tl_version}
Provides:       tex(yv1di8c.tfm) = %{tl_version}, tex(yv1di8t.tfm) = %{tl_version}
Provides:       tex(yv1h8c.tfm) = %{tl_version}, tex(yv1h8t.tfm) = %{tl_version}
Provides:       tex(yv1ho8c.tfm) = %{tl_version}, tex(yv1ho8t.tfm) = %{tl_version}
Provides:       tex(yv1l8c.tfm) = %{tl_version}, tex(yv1l8t.tfm) = %{tl_version}
Provides:       tex(yv1li8c.tfm) = %{tl_version}, tex(yv1li8t.tfm) = %{tl_version}
Provides:       tex(yv1r8c.tfm) = %{tl_version}, tex(yv1r8cc.tfm) = %{tl_version}
Provides:       tex(yv1r8cx.tfm) = %{tl_version}, tex(yv1r8t.tfm) = %{tl_version}
Provides:       tex(yv1r8tc.tfm) = %{tl_version}, tex(yv1r8tx.tfm) = %{tl_version}
Provides:       tex(yv1ri8c.tfm) = %{tl_version}, tex(yv1ri8cc.tfm) = %{tl_version}
Provides:       tex(yv1ri8cx.tfm) = %{tl_version}, tex(yv1ri8t.tfm) = %{tl_version}
Provides:       tex(yv1ri8tc.tfm) = %{tl_version}, tex(yv1ri8tx.tfm) = %{tl_version}
Provides:       tex(t1-yv3b-c.tfm) = %{tl_version}, tex(t1-yv3b-x.tfm) = %{tl_version}
Provides:       tex(t1-yv3b.tfm) = %{tl_version}, tex(t1-yv3bi-c.tfm) = %{tl_version}
Provides:       tex(t1-yv3bi-x.tfm) = %{tl_version}, tex(t1-yv3bi.tfm) = %{tl_version}
Provides:       tex(t1-yv3r-c.tfm) = %{tl_version}, tex(t1-yv3r-x.tfm) = %{tl_version}
Provides:       tex(t1-yv3r.tfm) = %{tl_version}, tex(t1-yv3ri-c.tfm) = %{tl_version}
Provides:       tex(t1-yv3ri-x.tfm) = %{tl_version}, tex(t1-yv3ri.tfm) = %{tl_version}
Provides:       tex(ts1-yv3b-c.tfm) = %{tl_version}, tex(ts1-yv3b-x.tfm) = %{tl_version}
Provides:       tex(ts1-yv3b.tfm) = %{tl_version}, tex(ts1-yv3bi-c.tfm) = %{tl_version}
Provides:       tex(ts1-yv3bi-x.tfm) = %{tl_version}, tex(ts1-yv3bi.tfm) = %{tl_version}
Provides:       tex(ts1-yv3r-c.tfm) = %{tl_version}, tex(ts1-yv3r-x.tfm) = %{tl_version}
Provides:       tex(ts1-yv3r.tfm) = %{tl_version}, tex(ts1-yv3ri-c.tfm) = %{tl_version}
Provides:       tex(ts1-yv3ri-x.tfm) = %{tl_version}, tex(ts1-yv3ri.tfm) = %{tl_version}
Provides:       tex(yv3b8c.tfm) = %{tl_version}, tex(yv3b8cc.tfm) = %{tl_version}
Provides:       tex(yv3b8cx.tfm) = %{tl_version}, tex(yv3b8t.tfm) = %{tl_version}
Provides:       tex(yv3b8tc.tfm) = %{tl_version}, tex(yv3b8tx.tfm) = %{tl_version}
Provides:       tex(yv3bi8c.tfm) = %{tl_version}, tex(yv3bi8cc.tfm) = %{tl_version}
Provides:       tex(yv3bi8cx.tfm) = %{tl_version}, tex(yv3bi8t.tfm) = %{tl_version}
Provides:       tex(yv3bi8tc.tfm) = %{tl_version}, tex(yv3bi8tx.tfm) = %{tl_version}
Provides:       tex(yv3r8c.tfm) = %{tl_version}, tex(yv3r8cc.tfm) = %{tl_version}
Provides:       tex(yv3r8cx.tfm) = %{tl_version}, tex(yv3r8t.tfm) = %{tl_version}
Provides:       tex(yv3r8tc.tfm) = %{tl_version}, tex(yv3r8tx.tfm) = %{tl_version}
Provides:       tex(yv3ri8c.tfm) = %{tl_version}, tex(yv3ri8cc.tfm) = %{tl_version}
Provides:       tex(yv3ri8cx.tfm) = %{tl_version}, tex(yv3ri8t.tfm) = %{tl_version}
Provides:       tex(yv3ri8tc.tfm) = %{tl_version}, tex(yv3ri8tx.tfm) = %{tl_version}
Provides:       tex(yvtb8a.pfb) = %{tl_version}, tex(yvtb8ac.pfb) = %{tl_version}
Provides:       tex(yvtbc8a.pfb) = %{tl_version}, tex(yvtbc8ac.pfb) = %{tl_version}
Provides:       tex(yvtbci8a.pfb) = %{tl_version}, tex(yvtbci8ac.pfb) = %{tl_version}
Provides:       tex(yvtbd8ac.pfb) = %{tl_version}, tex(yvtbi8a.pfb) = %{tl_version}
Provides:       tex(yvtbi8ac.pfb) = %{tl_version}, tex(yvth8a.pfb) = %{tl_version}
Provides:       tex(yvthi8a.pfb) = %{tl_version}, tex(yvtr8a.pfb) = %{tl_version}
Provides:       tex(yvtr8ac.pfb) = %{tl_version}, tex(yvtrc8a.pfb) = %{tl_version}
Provides:       tex(yvtrc8ac.pfb) = %{tl_version}, tex(yvtrci8a.pfb) = %{tl_version}
Provides:       tex(yvtrci8ac.pfb) = %{tl_version}, tex(yvtrdl8a.pfb) = %{tl_version}
Provides:       tex(yvtri8a.pfb) = %{tl_version}, tex(yvtri8ac.pfb) = %{tl_version}
Provides:       tex(yv2b8a.pfb) = %{tl_version}, tex(yv2b8ac.pfb) = %{tl_version}
Provides:       tex(yv2bi8a.pfb) = %{tl_version}, tex(yv2bi8ac.pfb) = %{tl_version}
Provides:       tex(yv2m8a.pfb) = %{tl_version}, tex(yv2mi8a.pfb) = %{tl_version}
Provides:       tex(yv2r8a.pfb) = %{tl_version}, tex(yv2r8ac.pfb) = %{tl_version}
Provides:       tex(yv2ri8a.pfb) = %{tl_version}, tex(yv2ri8ac.pfb) = %{tl_version}
Provides:       tex(yv2x8a.pfb) = %{tl_version}, tex(yv2xi8a.pfb) = %{tl_version}
Provides:       tex(yvob8a.pfb) = %{tl_version}, tex(yvobi8a.pfb) = %{tl_version}
Provides:       tex(yvodd8a.pfb) = %{tl_version}, tex(yvor8a.pfb) = %{tl_version}
Provides:       tex(yvori8a.pfb) = %{tl_version}, tex(yv1b8a.pfb) = %{tl_version}
Provides:       tex(yv1b8ac.pfb) = %{tl_version}, tex(yv1b8ax.pfb) = %{tl_version}
Provides:       tex(yv1bd8a.pfb) = %{tl_version}, tex(yv1bi8a.pfb) = %{tl_version}
Provides:       tex(yv1bi8ac.pfb) = %{tl_version}, tex(yv1bi8ax.pfb) = %{tl_version}
Provides:       tex(yv1d8a.pfb) = %{tl_version}, tex(yv1dd8au.pfb) = %{tl_version}
Provides:       tex(yv1di8a.pfb) = %{tl_version}, tex(yv1h8a.pfb) = %{tl_version}
Provides:       tex(yv1ho8a.pfb) = %{tl_version}, tex(yv1l8a.pfb) = %{tl_version}
Provides:       tex(yv1li8a.pfb) = %{tl_version}, tex(yv1r8a.pfb) = %{tl_version}
Provides:       tex(yv1r8ac.pfb) = %{tl_version}, tex(yv1r8ax.pfb) = %{tl_version}
Provides:       tex(yv1ri8a.pfb) = %{tl_version}, tex(yv1ri8ac.pfb) = %{tl_version}
Provides:       tex(yv1ri8ax.pfb) = %{tl_version}, tex(yv3b8a.pfb) = %{tl_version}
Provides:       tex(yv3b8ac.pfb) = %{tl_version}, tex(yv3b8ax.pfb) = %{tl_version}
Provides:       tex(yv3bi8a.pfb) = %{tl_version}, tex(yv3bi8ac.pfb) = %{tl_version}
Provides:       tex(yv3bi8ax.pfb) = %{tl_version}, tex(yv3r8a.pfb) = %{tl_version}
Provides:       tex(yv3r8ac.pfb) = %{tl_version}, tex(yv3r8ax.pfb) = %{tl_version}
Provides:       tex(yv3ri8a.pfb) = %{tl_version}, tex(yv3ri8ac.pfb) = %{tl_version}
Provides:       tex(yv3ri8ax.pfb) = %{tl_version}, tex(yvtb8c.vf) = %{tl_version}
Provides:       tex(yvtb8cc.vf) = %{tl_version}, tex(yvtb8t.vf) = %{tl_version}
Provides:       tex(yvtb8tc.vf) = %{tl_version}, tex(yvtbc8c.vf) = %{tl_version}
Provides:       tex(yvtbc8cc.vf) = %{tl_version}, tex(yvtbc8t.vf) = %{tl_version}
Provides:       tex(yvtbc8tc.vf) = %{tl_version}, tex(yvtbci8c.vf) = %{tl_version}
Provides:       tex(yvtbci8cc.vf) = %{tl_version}, tex(yvtbci8t.vf) = %{tl_version}
Provides:       tex(yvtbci8tc.vf) = %{tl_version}, tex(yvtbcij8t.vf) = %{tl_version}
Provides:       tex(yvtbcij8tc.vf) = %{tl_version}, tex(yvtbcijw8t.vf) = %{tl_version}
Provides:       tex(yvtbcijw8tc.vf) = %{tl_version}, tex(yvtbciw8t.vf) = %{tl_version}
Provides:       tex(yvtbciw8tc.vf) = %{tl_version}, tex(yvtbcj8t.vf) = %{tl_version}
Provides:       tex(yvtbcj8tc.vf) = %{tl_version}, tex(yvtbcjw8t.vf) = %{tl_version}
Provides:       tex(yvtbcjw8tc.vf) = %{tl_version}, tex(yvtbcw8t.vf) = %{tl_version}
Provides:       tex(yvtbcw8tc.vf) = %{tl_version}, tex(yvtbd8cc.vf) = %{tl_version}
Provides:       tex(yvtbd8tc.vf) = %{tl_version}, tex(yvtbi8c.vf) = %{tl_version}
Provides:       tex(yvtbi8cc.vf) = %{tl_version}, tex(yvtbi8t.vf) = %{tl_version}
Provides:       tex(yvtbi8tc.vf) = %{tl_version}, tex(yvtbij8t.vf) = %{tl_version}
Provides:       tex(yvtbij8tc.vf) = %{tl_version}, tex(yvtbijw8t.vf) = %{tl_version}
Provides:       tex(yvtbijw8tc.vf) = %{tl_version}, tex(yvtbiw8t.vf) = %{tl_version}
Provides:       tex(yvtbiw8tc.vf) = %{tl_version}, tex(yvtbj8t.vf) = %{tl_version}
Provides:       tex(yvtbj8tc.vf) = %{tl_version}, tex(yvtbjw8t.vf) = %{tl_version}
Provides:       tex(yvtbjw8tc.vf) = %{tl_version}, tex(yvtbw8t.vf) = %{tl_version}
Provides:       tex(yvtbw8tc.vf) = %{tl_version}, tex(yvth8c.vf) = %{tl_version}
Provides:       tex(yvth8t.vf) = %{tl_version}, tex(yvthi8c.vf) = %{tl_version}
Provides:       tex(yvthi8t.vf) = %{tl_version}, tex(yvtr8c.vf) = %{tl_version}
Provides:       tex(yvtr8cc.vf) = %{tl_version}, tex(yvtr8t.vf) = %{tl_version}
Provides:       tex(yvtr8tc.vf) = %{tl_version}, tex(yvtrajw8t.vf) = %{tl_version}
Provides:       tex(yvtraw8t.vf) = %{tl_version}, tex(yvtrc8c.vf) = %{tl_version}
Provides:       tex(yvtrc8cc.vf) = %{tl_version}, tex(yvtrc8t.vf) = %{tl_version}
Provides:       tex(yvtrc8tc.vf) = %{tl_version}, tex(yvtrci8c.vf) = %{tl_version}
Provides:       tex(yvtrci8cc.vf) = %{tl_version}, tex(yvtrci8t.vf) = %{tl_version}
Provides:       tex(yvtrci8tc.vf) = %{tl_version}, tex(yvtrcij8t.vf) = %{tl_version}
Provides:       tex(yvtrcij8tc.vf) = %{tl_version}, tex(yvtrcijw8t.vf) = %{tl_version}
Provides:       tex(yvtrcijw8tc.vf) = %{tl_version}, tex(yvtrciw8t.vf) = %{tl_version}
Provides:       tex(yvtrciw8tc.vf) = %{tl_version}, tex(yvtrcj8t.vf) = %{tl_version}
Provides:       tex(yvtrcj8tc.vf) = %{tl_version}, tex(yvtrcjw8t.vf) = %{tl_version}
Provides:       tex(yvtrcjw8tc.vf) = %{tl_version}, tex(yvtrcw8t.vf) = %{tl_version}
Provides:       tex(yvtrcw8tc.vf) = %{tl_version}, tex(yvtrdl8c.vf) = %{tl_version}
Provides:       tex(yvtrdl8t.vf) = %{tl_version}, tex(yvtri8c.vf) = %{tl_version}
Provides:       tex(yvtri8cc.vf) = %{tl_version}, tex(yvtri8t.vf) = %{tl_version}
Provides:       tex(yvtri8tc.vf) = %{tl_version}, tex(yvtrij8t.vf) = %{tl_version}
Provides:       tex(yvtrij8tc.vf) = %{tl_version}, tex(yvtrijw8t.vf) = %{tl_version}
Provides:       tex(yvtrijw8tc.vf) = %{tl_version}, tex(yvtriw8t.vf) = %{tl_version}
Provides:       tex(yvtriw8tc.vf) = %{tl_version}, tex(yvtrj8t.vf) = %{tl_version}
Provides:       tex(yvtrj8tc.vf) = %{tl_version}, tex(yvtrjw8t.vf) = %{tl_version}
Provides:       tex(yvtrjw8tc.vf) = %{tl_version}, tex(yvtrw8t.vf) = %{tl_version}
Provides:       tex(yvtrw8tc.vf) = %{tl_version}, tex(yv2b8c.vf) = %{tl_version}
Provides:       tex(yv2b8cc.vf) = %{tl_version}, tex(yv2b8t.vf) = %{tl_version}
Provides:       tex(yv2b8tc.vf) = %{tl_version}, tex(yv2bi8c.vf) = %{tl_version}
Provides:       tex(yv2bi8cc.vf) = %{tl_version}, tex(yv2bi8t.vf) = %{tl_version}
Provides:       tex(yv2bi8tc.vf) = %{tl_version}, tex(yv2m8c.vf) = %{tl_version}
Provides:       tex(yv2m8t.vf) = %{tl_version}, tex(yv2mi8c.vf) = %{tl_version}
Provides:       tex(yv2mi8t.vf) = %{tl_version}, tex(yv2r8c.vf) = %{tl_version}
Provides:       tex(yv2r8cc.vf) = %{tl_version}, tex(yv2r8t.vf) = %{tl_version}
Provides:       tex(yv2r8tc.vf) = %{tl_version}, tex(yv2ri8c.vf) = %{tl_version}
Provides:       tex(yv2ri8cc.vf) = %{tl_version}, tex(yv2ri8t.vf) = %{tl_version}
Provides:       tex(yv2ri8tc.vf) = %{tl_version}, tex(yv2x8c.vf) = %{tl_version}
Provides:       tex(yv2x8t.vf) = %{tl_version}, tex(yv2xi8c.vf) = %{tl_version}
Provides:       tex(yv2xi8t.vf) = %{tl_version}, tex(yvoab8t.vf) = %{tl_version}
Provides:       tex(yvoabi8t.vf) = %{tl_version}, tex(yvoar8t.vf) = %{tl_version}
Provides:       tex(yvoari8t.vf) = %{tl_version}, tex(yvob8c.vf) = %{tl_version}
Provides:       tex(yvob8t.vf) = %{tl_version}, tex(yvobi8c.vf) = %{tl_version}
Provides:       tex(yvobi8t.vf) = %{tl_version}, tex(yvodd8c.vf) = %{tl_version}
Provides:       tex(yvodd8t.vf) = %{tl_version}, tex(yvor8c.vf) = %{tl_version}
Provides:       tex(yvor8t.vf) = %{tl_version}, tex(yvori8c.vf) = %{tl_version}
Provides:       tex(yvori8t.vf) = %{tl_version}, tex(yv1b8c.vf) = %{tl_version}
Provides:       tex(yv1b8cc.vf) = %{tl_version}, tex(yv1b8cx.vf) = %{tl_version}
Provides:       tex(yv1b8t.vf) = %{tl_version}, tex(yv1b8tc.vf) = %{tl_version}
Provides:       tex(yv1b8tx.vf) = %{tl_version}, tex(yv1bd8c.vf) = %{tl_version}
Provides:       tex(yv1bd8t.vf) = %{tl_version}, tex(yv1bi8c.vf) = %{tl_version}
Provides:       tex(yv1bi8cc.vf) = %{tl_version}, tex(yv1bi8cx.vf) = %{tl_version}
Provides:       tex(yv1bi8t.vf) = %{tl_version}, tex(yv1bi8tc.vf) = %{tl_version}
Provides:       tex(yv1bi8tx.vf) = %{tl_version}, tex(yv1d8c.vf) = %{tl_version}
Provides:       tex(yv1d8t.vf) = %{tl_version}, tex(yv1dd8cu.vf) = %{tl_version}
Provides:       tex(yv1dd8tu.vf) = %{tl_version}, tex(yv1di8c.vf) = %{tl_version}
Provides:       tex(yv1di8t.vf) = %{tl_version}, tex(yv1h8c.vf) = %{tl_version}
Provides:       tex(yv1h8t.vf) = %{tl_version}, tex(yv1ho8c.vf) = %{tl_version}
Provides:       tex(yv1ho8t.vf) = %{tl_version}, tex(yv1l8c.vf) = %{tl_version}
Provides:       tex(yv1l8t.vf) = %{tl_version}, tex(yv1li8c.vf) = %{tl_version}
Provides:       tex(yv1li8t.vf) = %{tl_version}, tex(yv1r8c.vf) = %{tl_version}
Provides:       tex(yv1r8cc.vf) = %{tl_version}, tex(yv1r8cx.vf) = %{tl_version}
Provides:       tex(yv1r8t.vf) = %{tl_version}, tex(yv1r8tc.vf) = %{tl_version}
Provides:       tex(yv1r8tx.vf) = %{tl_version}, tex(yv1ri8c.vf) = %{tl_version}
Provides:       tex(yv1ri8cc.vf) = %{tl_version}, tex(yv1ri8cx.vf) = %{tl_version}
Provides:       tex(yv1ri8t.vf) = %{tl_version}, tex(yv1ri8tc.vf) = %{tl_version}
Provides:       tex(yv1ri8tx.vf) = %{tl_version}, tex(yv3b8c.vf) = %{tl_version}
Provides:       tex(yv3b8cc.vf) = %{tl_version}, tex(yv3b8cx.vf) = %{tl_version}
Provides:       tex(yv3b8t.vf) = %{tl_version}, tex(yv3b8tc.vf) = %{tl_version}
Provides:       tex(yv3b8tx.vf) = %{tl_version}, tex(yv3bi8c.vf) = %{tl_version}
Provides:       tex(yv3bi8cc.vf) = %{tl_version}, tex(yv3bi8cx.vf) = %{tl_version}
Provides:       tex(yv3bi8t.vf) = %{tl_version}, tex(yv3bi8tc.vf) = %{tl_version}
Provides:       tex(yv3bi8tx.vf) = %{tl_version}, tex(yv3r8c.vf) = %{tl_version}
Provides:       tex(yv3r8cc.vf) = %{tl_version}, tex(yv3r8cx.vf) = %{tl_version}
Provides:       tex(yv3r8t.vf) = %{tl_version}, tex(yv3r8tc.vf) = %{tl_version}
Provides:       tex(yv3r8tx.vf) = %{tl_version}, tex(yv3ri8c.vf) = %{tl_version}
Provides:       tex(yv3ri8cc.vf) = %{tl_version}, tex(yv3ri8cx.vf) = %{tl_version}
Provides:       tex(yv3ri8t.vf) = %{tl_version}, tex(yv3ri8tc.vf) = %{tl_version}
Provides:       tex(yv3ri8tx.vf) = %{tl_version}, tex(t1yvt.fd) = %{tl_version}
Provides:       tex(t1yvtajw.fd) = %{tl_version}, tex(t1yvtaw.fd) = %{tl_version}
Provides:       tex(t1yvtd.fd) = %{tl_version}, tex(t1yvtj.fd) = %{tl_version}
Provides:       tex(t1yvtjw.fd) = %{tl_version}, tex(t1yvtw.fd) = %{tl_version}
Provides:       tex(ts1yvt.fd) = %{tl_version}, tex(ts1yvtajw.fd) = %{tl_version}
Provides:       tex(ts1yvtaw.fd) = %{tl_version}, tex(ts1yvtd.fd) = %{tl_version}
Provides:       tex(ts1yvtj.fd) = %{tl_version}, tex(ts1yvtjw.fd) = %{tl_version}
Provides:       tex(ts1yvtw.fd) = %{tl_version}, tex(t1yv2.fd) = %{tl_version}
Provides:       tex(ts1yv2.fd) = %{tl_version}, tex(venturis.sty) = %{tl_version}
Provides:       tex(venturis2.sty) = %{tl_version}, tex(venturisold.sty) = %{tl_version}
Provides:       tex(t1yvo.fd) = %{tl_version}, tex(t1yvoa.fd) = %{tl_version}
Provides:       tex(t1yvoad.fd) = %{tl_version}, tex(t1yvod.fd) = %{tl_version}
Provides:       tex(ts1yvo.fd) = %{tl_version}, tex(ts1yvoa.fd) = %{tl_version}
Provides:       tex(ts1yvoad.fd) = %{tl_version}, tex(ts1yvod.fd) = %{tl_version}
Provides:       tex(t1yv1.fd) = %{tl_version}, tex(t1yv1d.fd) = %{tl_version}
Provides:       tex(ts1yv1.fd) = %{tl_version}, tex(ts1yv1d.fd) = %{tl_version}
Provides:       tex(t1yv3.fd) = %{tl_version}, tex(ts1yv3.fd) = %{tl_version}

%description -n texlive-venturisadf
Serif and sans serif complete text font families, in both Adobe
Type 1 and OpenType formats for publication. The family is
based on Utopia family, and has been modified and developed by
the Arkandis Digital foundry. Support for using the fonts, in
LaTeX, is also provided (and makes use of the nfssext-cfr
package).

%package -n texlive-venturisadf-doc
Summary:        Documentation for venturisadf
Version:        svn19444.1.005

Provides:       tex-venturisadf-doc
AutoReqProv:    No

%description -n texlive-venturisadf-doc
Documentation for venturisadf

%package -n texlive-wsuipa
Provides:       tex-wsuipa = %{tl_version}
License:        Utopia
Summary:        International Phonetic Alphabet fonts
Version:        svn25469.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(wbxipa10.tfm) = %{tl_version}, tex(wbxipa11.tfm) = %{tl_version}
Provides:       tex(wbxipa12.tfm) = %{tl_version}, tex(wbxipa17.tfm) = %{tl_version}
Provides:       tex(wbxipa8.tfm) = %{tl_version}, tex(wbxipa9.tfm) = %{tl_version}
Provides:       tex(wslipa10.tfm) = %{tl_version}, tex(wslipa11.tfm) = %{tl_version}
Provides:       tex(wslipa12.tfm) = %{tl_version}, tex(wslipa17.tfm) = %{tl_version}
Provides:       tex(wslipa8.tfm) = %{tl_version}, tex(wslipa9.tfm) = %{tl_version}
Provides:       tex(wsuipa10.tfm) = %{tl_version}, tex(wsuipa11.tfm) = %{tl_version}
Provides:       tex(wsuipa12.tfm) = %{tl_version}, tex(wsuipa17.tfm) = %{tl_version}
Provides:       tex(wsuipa8.tfm) = %{tl_version}, tex(wsuipa9.tfm) = %{tl_version}
Provides:       tex(ipa.sty) = %{tl_version}, tex(ipalmacs.sty) = %{tl_version}
Provides:       tex(uipa.fd) = %{tl_version}

%description -n texlive-wsuipa
The package provides a 7-bit IPA font, as Metafont source, and
macros for support under TeXt1 and LaTeX. The fonts (and
macros) are now largely superseded by the tipa fonts.

%package -n texlive-wsuipa-doc
Summary:        Documentation for wsuipa
Version:        svn25469.0

Provides:       tex-wsuipa-doc
AutoReqProv:    No

%description -n texlive-wsuipa-doc
Documentation for wsuipa

%package -n texlive-utopia
Provides:       tex-utopia = %{tl_version}
License:        Utopia
Summary:        Adobe Utopia fonts
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(putb7t.tfm) = %{tl_version}, tex(putb8c.tfm) = %{tl_version}
Provides:       tex(putb8r.tfm) = %{tl_version}, tex(putb8t.tfm) = %{tl_version}
Provides:       tex(putbc7t.tfm) = %{tl_version}, tex(putbc8t.tfm) = %{tl_version}
Provides:       tex(putbi7t.tfm) = %{tl_version}, tex(putbi8c.tfm) = %{tl_version}
Provides:       tex(putbi8r.tfm) = %{tl_version}, tex(putbi8t.tfm) = %{tl_version}
Provides:       tex(putbo7t.tfm) = %{tl_version}, tex(putbo8c.tfm) = %{tl_version}
Provides:       tex(putbo8r.tfm) = %{tl_version}, tex(putbo8t.tfm) = %{tl_version}
Provides:       tex(putr7t.tfm) = %{tl_version}, tex(putr8c.tfm) = %{tl_version}
Provides:       tex(putr8r.tfm) = %{tl_version}, tex(putr8t.tfm) = %{tl_version}
Provides:       tex(putrc7t.tfm) = %{tl_version}, tex(putrc8t.tfm) = %{tl_version}
Provides:       tex(putri7t.tfm) = %{tl_version}, tex(putri8c.tfm) = %{tl_version}
Provides:       tex(putri8r.tfm) = %{tl_version}, tex(putri8t.tfm) = %{tl_version}
Provides:       tex(putro7t.tfm) = %{tl_version}, tex(putro8c.tfm) = %{tl_version}
Provides:       tex(putro8r.tfm) = %{tl_version}, tex(putro8t.tfm) = %{tl_version}
Provides:       tex(putb8a.pfb) = %{tl_version}, tex(putbi8a.pfb) = %{tl_version}
Provides:       tex(putr8a.pfb) = %{tl_version}, tex(putri8a.pfb) = %{tl_version}
Provides:       tex(putb7t.vf) = %{tl_version}, tex(putb8c.vf) = %{tl_version}
Provides:       tex(putb8t.vf) = %{tl_version}, tex(putbc7t.vf) = %{tl_version}
Provides:       tex(putbc8t.vf) = %{tl_version}, tex(putbi7t.vf) = %{tl_version}
Provides:       tex(putbi8c.vf) = %{tl_version}, tex(putbi8t.vf) = %{tl_version}
Provides:       tex(putbo7t.vf) = %{tl_version}, tex(putbo8c.vf) = %{tl_version}
Provides:       tex(putbo8t.vf) = %{tl_version}, tex(putr7t.vf) = %{tl_version}
Provides:       tex(putr8c.vf) = %{tl_version}, tex(putr8t.vf) = %{tl_version}
Provides:       tex(putrc7t.vf) = %{tl_version}, tex(putrc8t.vf) = %{tl_version}
Provides:       tex(putri7t.vf) = %{tl_version}, tex(putri8c.vf) = %{tl_version}
Provides:       tex(putri8t.vf) = %{tl_version}, tex(putro7t.vf) = %{tl_version}
Provides:       tex(putro8c.vf) = %{tl_version}, tex(putro8t.vf) = %{tl_version}

%description -n texlive-utopia
The Adobe Standard Encoding set (upright and italic shapes,
medium and bold weights) of the Utopia font family, which Adobe
donated to the X Consortium. Macro support, and maths fonts
that match the Utopia family, are provided by the Fourier and
the Mathdesign font packages.

%package -n texlive-utopia-doc
Summary:        Documentation for utopia
Version:        svn15878.0

Provides:       tex-utopia-doc
AutoReqProv:    No

%description -n texlive-utopia-doc
Documentation for utopia

%package -n texlive-wasy
Provides:       tex-wasy = %{tl_version}
License:        Public Domain
Summary:        The wasy fonts (Waldi symbol fonts)
Version:        svn35831.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(wasy10.tfm) = %{tl_version}, tex(wasy5.tfm) = %{tl_version}
Provides:       tex(wasy6.tfm) = %{tl_version}, tex(wasy7.tfm) = %{tl_version}
Provides:       tex(wasy8.tfm) = %{tl_version}, tex(wasy9.tfm) = %{tl_version}
Provides:       tex(wasyb10.tfm) = %{tl_version}, tex(wasyfont.tex) = %{tl_version}

%description -n texlive-wasy
These are the wasy (Waldi symbol) fonts, second release. This
bundle presents the fonts in Metafont format, but they are also
available in Adobe Type 1 format. Support under LaTeX is
provided by the wasysym package.

%package -n texlive-wasy-doc
Summary:        Documentation for wasy
Version:        svn35831.0

Provides:       tex-wasy-doc
AutoReqProv:    No

%description -n texlive-wasy-doc
Documentation for wasy

%package -n texlive-wasy2-ps
Provides:       tex-wasy2-ps = %{tl_version}
License:        Public Domain
Summary:        Type 1 versions of wasy2 fonts
Version:        svn35830.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex-wasy
Provides:       tex(wasy.map) = %{tl_version}, tex(wasy10.pfb) = %{tl_version}
Provides:       tex(wasy5.pfb) = %{tl_version}, tex(wasy6.pfb) = %{tl_version}
Provides:       tex(wasy7.pfb) = %{tl_version}, tex(wasy8.pfb) = %{tl_version}
Provides:       tex(wasy9.pfb) = %{tl_version}, tex(wasyb10.pfb) = %{tl_version}

%description -n texlive-wasy2-ps
Converted (Adobe Type 1) outlines of (some of) the wasy2 fonts.

%package -n texlive-wasy2-ps-doc
Summary:        Documentation for wasy2-ps
Version:        svn35830.0

Provides:       tex-wasy2-ps-doc
AutoReqProv:    No
Requires:       tex-wasy-doc

%description -n texlive-wasy2-ps-doc
Documentation for wasy2-ps

%package -n texlive-wasysym
Provides:       tex-wasysym = %{tl_version}
License:        LPPL
Summary:        LaTeX support file to use the WASY2 fonts
Version:        svn15878.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(uwasy.fd) = %{tl_version}, tex(uwasyvar.fd) = %{tl_version}
Provides:       tex(wasysym.sty) = %{tl_version}

%description -n texlive-wasysym
The WASY2 (Waldi Symbol) font by Roland Waldi provides many
glyphs like male and female symbols and astronomical symbols,
as well as the complete lasy font set and other odds and ends.
The wasysym package implements an easy to use interface for
these symbols.

%package -n texlive-wasysym-doc
Summary:        Documentation for wasysym
Version:        svn15878.2.0

Provides:       tex-wasysym-doc
AutoReqProv:    No

%description -n texlive-wasysym-doc
Documentation for wasysym

%package -n texlive-upca
Provides:       tex-upca = %{tl_version}
License:        LPPL
Summary:        Print UPC-A barcodes
Version:        svn22511.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(upca.tex) = %{tl_version}

%description -n texlive-upca
The package defines a single macro \upca, to print UPC-A
barcodes.

%package -n texlive-upca-doc
Summary:        Documentation for upca
Version:        svn22511.0

Provides:       tex-upca-doc
AutoReqProv:    No

%description -n texlive-upca-doc
Documentation for upca

%package -n texlive-uptex-base
Provides:       tex-uptex-base = %{tl_version}
License:        BSD
Summary:        Plain TeX format and documents for upTeX
Version:        svn46733
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(euptex.ini) = %{tl_version}, tex(ukinsoku.tex) = %{tl_version}
Provides:       tex(uptex.ini) = %{tl_version}, tex(uptex.tex) = %{tl_version}

%description -n texlive-uptex-base
The bundle contains plain TeX format and documents for upTeX.

%package -n texlive-uptex-base-doc
Summary:        Documentation for uptex-base
Version:        svn46733
Provides:       tex-uptex-base-doc
AutoReqProv:    No

%description -n texlive-uptex-base-doc
Documentation for uptex-base

%package -n texlive-uptex-fonts
Provides:       tex-uptex-fonts = %{tl_version}
License:        BSD
Summary:        Fonts for use with upTeX
Version:        svn47162
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(upgbm-h.tfm) = %{tl_version}, tex(upgbm-hq.tfm) = %{tl_version}
Provides:       tex(upgbm-v.tfm) = %{tl_version}, tex(uphygt-h.tfm) = %{tl_version}
Provides:       tex(uphygt-v.tfm) = %{tl_version}, tex(uphysmjm-h.tfm) = %{tl_version}
Provides:       tex(uphysmjm-v.tfm) = %{tl_version}, tex(upjisg-h.tfm) = %{tl_version}
Provides:       tex(upjisg-hq.tfm) = %{tl_version}, tex(upjisg-v.tfm) = %{tl_version}
Provides:       tex(upjisr-h.tfm) = %{tl_version}, tex(upjisr-hq.tfm) = %{tl_version}
Provides:       tex(upjisr-v.tfm) = %{tl_version}, tex(upjpngt-h.tfm) = %{tl_version}
Provides:       tex(upjpngt-v.tfm) = %{tl_version}, tex(upjpnrm-h.tfm) = %{tl_version}
Provides:       tex(upjpnrm-v.tfm) = %{tl_version}, tex(upkorgt-h.tfm) = %{tl_version}
Provides:       tex(upkorgt-v.tfm) = %{tl_version}, tex(upkorrm-h.tfm) = %{tl_version}
Provides:       tex(upkorrm-v.tfm) = %{tl_version}, tex(upmhm-h.tfm) = %{tl_version}
Provides:       tex(upmhm-v.tfm) = %{tl_version}, tex(upmsl-h.tfm) = %{tl_version}
Provides:       tex(upmsl-v.tfm) = %{tl_version}, tex(uprml-h.tfm) = %{tl_version}
Provides:       tex(uprml-hq.tfm) = %{tl_version}, tex(uprml-v.tfm) = %{tl_version}
Provides:       tex(upschgt-h.tfm) = %{tl_version}, tex(upschgt-v.tfm) = %{tl_version}
Provides:       tex(upschrm-h.tfm) = %{tl_version}, tex(upschrm-v.tfm) = %{tl_version}
Provides:       tex(upstht-h.tfm) = %{tl_version}, tex(upstht-v.tfm) = %{tl_version}
Provides:       tex(upstsl-h.tfm) = %{tl_version}, tex(upstsl-v.tfm) = %{tl_version}
Provides:       tex(uptchgt-h.tfm) = %{tl_version}, tex(uptchgt-v.tfm) = %{tl_version}
Provides:       tex(uptchrm-h.tfm) = %{tl_version}, tex(uptchrm-v.tfm) = %{tl_version}
Provides:       tex(ugbm.tfm) = %{tl_version}, tex(ugbmv.tfm) = %{tl_version}
Provides:       tex(ugoth10.tfm) = %{tl_version}, tex(umin10.tfm) = %{tl_version}
Provides:       tex(urml.tfm) = %{tl_version}, tex(urmlv.tfm) = %{tl_version}
Provides:       tex(utgoth10.tfm) = %{tl_version}, tex(utmin10.tfm) = %{tl_version}
Provides:       tex(upjisg-h.vf) = %{tl_version}, tex(upjisg-hq.vf) = %{tl_version}
Provides:       tex(upjisg-v.vf) = %{tl_version}, tex(upjisr-h.vf) = %{tl_version}
Provides:       tex(upjisr-hq.vf) = %{tl_version}, tex(upjisr-v.vf) = %{tl_version}
Provides:       tex(upjpngt-h.vf) = %{tl_version}, tex(upjpngt-v.vf) = %{tl_version}
Provides:       tex(upjpnrm-h.vf) = %{tl_version}, tex(upjpnrm-v.vf) = %{tl_version}
Provides:       tex(upkorgt-h.vf) = %{tl_version}, tex(upkorgt-v.vf) = %{tl_version}
Provides:       tex(upkorrm-h.vf) = %{tl_version}, tex(upkorrm-v.vf) = %{tl_version}
Provides:       tex(upschgt-h.vf) = %{tl_version}, tex(upschgt-v.vf) = %{tl_version}
Provides:       tex(upschrm-h.vf) = %{tl_version}, tex(upschrm-v.vf) = %{tl_version}
Provides:       tex(uptchgt-h.vf) = %{tl_version}, tex(uptchgt-v.vf) = %{tl_version}
Provides:       tex(uptchrm-h.vf) = %{tl_version}, tex(uptchrm-v.vf) = %{tl_version}
Provides:       tex(ugoth10.vf) = %{tl_version}, tex(umin10.vf) = %{tl_version}
Provides:       tex(utgoth10.vf) = %{tl_version}, tex(utmin10.vf) = %{tl_version}
Provides:       tex(jt2gt.fd) = %{tl_version}, tex(jt2mc.fd) = %{tl_version}
Provides:       tex(jy2gt.fd) = %{tl_version}, tex(jy2mc.fd) = %{tl_version}

%description -n texlive-uptex-fonts
The bundle contains fonts (TFM and VF) for use with upTeX. This
is a redistribution derived from the upTeX distribution by
Takuji Tanaka.

%package -n texlive-uptex-fonts-doc
Summary:        Documentation for uptex-fonts
Version:        svn47162
Provides:       tex-uptex-fonts-doc
AutoReqProv:    No

%description -n texlive-uptex-fonts-doc
Documentation for uptex-fonts

%package -n texlive-underscore
Provides:       tex-underscore = %{tl_version}
License:        LPPL
Summary:        Control the behaviour of "_" in text
Version:        svn18261.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(underscore.sty) = %{tl_version}

%description -n texlive-underscore
With the package, \_ in text mode (i.e., \textunderscore)
prints an underscore so that hyphenation of words either side
of it is not affected; a package option controls whether an
actual hyphenation point appears after the underscore, or
merely a break point. The package also arranges that, while in
text, '_' itself behaves as \textunderscore (the behaviour of _
in maths mode is not affected).

%package -n texlive-underscore-doc
Summary:        Documentation for underscore
Version:        svn18261.0

Provides:       tex-underscore-doc
AutoReqProv:    No

%description -n texlive-underscore-doc
Documentation for underscore

%package -n texlive-uassign
Provides:       tex-uassign = %{tl_version}
License:        GPLv2+
Summary:        Provides environments and options for typesetting university assignments
Version:        svn38459

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(uassign.sty) = %{tl_version}

%description -n texlive-uassign
Provides environments and options for typesetting university
assignments

%package -n texlive-uassign-doc
Summary:        Documentation for uassign
Version:        svn38459

Provides:       tex-uassign-doc
AutoReqProv:    No

%description -n texlive-uassign-doc
Documentation for uassign

%package -n texlive-ucharcat
Provides:       tex-ucharcat = %{tl_version}
License:        LPPL
Summary:        Implementation of the (new in 2015) XeTeX \Ucharcat command in lua, for LuaTeX
Version:        svn38907

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ucharcat.sty) = %{tl_version}

%description -n texlive-ucharcat
The package implements the \Ucharcat command for LuaLaTeX.
\Ucharcat is a new primitive in XeTeX, an extension of the
existing \Uchar command, that allows the specification of the
catcode as well as character code of the character token being
constructed.

%package -n texlive-ucharcat-doc
Summary:        Documentation for ucharcat
Version:        svn38907

Provides:       tex-ucharcat-doc
AutoReqProv:    No

%description -n texlive-ucharcat-doc
Documentation for ucharcat

%package -n texlive-ucs
Provides:       tex-ucs = %{tl_version}
License:        LPPL 1.3
Summary:        Extended UTF-8 input encoding support for LaTeX
Version:        svn35853.2.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(hyperref.sty), tex(keyval.sty), tex(fontenc.sty)
Provides:       tex(uni-0.def) = %{tl_version}, tex(uni-1.def) = %{tl_version}
Provides:       tex(uni-100.def) = %{tl_version}, tex(uni-101.def) = %{tl_version}
Provides:       tex(uni-102.def) = %{tl_version}, tex(uni-103.def) = %{tl_version}
Provides:       tex(uni-104.def) = %{tl_version}, tex(uni-105.def) = %{tl_version}
Provides:       tex(uni-106.def) = %{tl_version}, tex(uni-107.def) = %{tl_version}
Provides:       tex(uni-108.def) = %{tl_version}, tex(uni-109.def) = %{tl_version}
Provides:       tex(uni-110.def) = %{tl_version}, tex(uni-111.def) = %{tl_version}
Provides:       tex(uni-112.def) = %{tl_version}, tex(uni-113.def) = %{tl_version}
Provides:       tex(uni-114.def) = %{tl_version}, tex(uni-115.def) = %{tl_version}
Provides:       tex(uni-116.def) = %{tl_version}, tex(uni-117.def) = %{tl_version}
Provides:       tex(uni-118.def) = %{tl_version}, tex(uni-119.def) = %{tl_version}
Provides:       tex(uni-12.def) = %{tl_version}, tex(uni-120.def) = %{tl_version}
Provides:       tex(uni-121.def) = %{tl_version}, tex(uni-122.def) = %{tl_version}
Provides:       tex(uni-123.def) = %{tl_version}, tex(uni-124.def) = %{tl_version}
Provides:       tex(uni-125.def) = %{tl_version}, tex(uni-126.def) = %{tl_version}
Provides:       tex(uni-127.def) = %{tl_version}, tex(uni-128.def) = %{tl_version}
Provides:       tex(uni-129.def) = %{tl_version}, tex(uni-130.def) = %{tl_version}
Provides:       tex(uni-131.def) = %{tl_version}, tex(uni-132.def) = %{tl_version}
Provides:       tex(uni-133.def) = %{tl_version}, tex(uni-134.def) = %{tl_version}
Provides:       tex(uni-135.def) = %{tl_version}, tex(uni-136.def) = %{tl_version}
Provides:       tex(uni-137.def) = %{tl_version}, tex(uni-138.def) = %{tl_version}
Provides:       tex(uni-139.def) = %{tl_version}, tex(uni-14.def) = %{tl_version}
Provides:       tex(uni-140.def) = %{tl_version}, tex(uni-141.def) = %{tl_version}
Provides:       tex(uni-142.def) = %{tl_version}, tex(uni-143.def) = %{tl_version}
Provides:       tex(uni-144.def) = %{tl_version}, tex(uni-145.def) = %{tl_version}
Provides:       tex(uni-146.def) = %{tl_version}, tex(uni-147.def) = %{tl_version}
Provides:       tex(uni-148.def) = %{tl_version}, tex(uni-149.def) = %{tl_version}
Provides:       tex(uni-150.def) = %{tl_version}, tex(uni-151.def) = %{tl_version}
Provides:       tex(uni-152.def) = %{tl_version}, tex(uni-153.def) = %{tl_version}
Provides:       tex(uni-154.def) = %{tl_version}, tex(uni-155.def) = %{tl_version}
Provides:       tex(uni-156.def) = %{tl_version}, tex(uni-157.def) = %{tl_version}
Provides:       tex(uni-158.def) = %{tl_version}, tex(uni-159.def) = %{tl_version}
Provides:       tex(uni-167.def) = %{tl_version}, tex(uni-172.def) = %{tl_version}
Provides:       tex(uni-173.def) = %{tl_version}, tex(uni-174.def) = %{tl_version}
Provides:       tex(uni-175.def) = %{tl_version}, tex(uni-176.def) = %{tl_version}
Provides:       tex(uni-177.def) = %{tl_version}, tex(uni-178.def) = %{tl_version}
Provides:       tex(uni-179.def) = %{tl_version}, tex(uni-18.def) = %{tl_version}
Provides:       tex(uni-180.def) = %{tl_version}, tex(uni-181.def) = %{tl_version}
Provides:       tex(uni-182.def) = %{tl_version}, tex(uni-183.def) = %{tl_version}
Provides:       tex(uni-184.def) = %{tl_version}, tex(uni-185.def) = %{tl_version}
Provides:       tex(uni-186.def) = %{tl_version}, tex(uni-187.def) = %{tl_version}
Provides:       tex(uni-188.def) = %{tl_version}, tex(uni-189.def) = %{tl_version}
Provides:       tex(uni-19.def) = %{tl_version}, tex(uni-190.def) = %{tl_version}
Provides:       tex(uni-191.def) = %{tl_version}, tex(uni-192.def) = %{tl_version}
Provides:       tex(uni-193.def) = %{tl_version}, tex(uni-194.def) = %{tl_version}
Provides:       tex(uni-195.def) = %{tl_version}, tex(uni-196.def) = %{tl_version}
Provides:       tex(uni-197.def) = %{tl_version}, tex(uni-198.def) = %{tl_version}
Provides:       tex(uni-199.def) = %{tl_version}, tex(uni-2.def) = %{tl_version}
Provides:       tex(uni-200.def) = %{tl_version}, tex(uni-201.def) = %{tl_version}
Provides:       tex(uni-202.def) = %{tl_version}, tex(uni-203.def) = %{tl_version}
Provides:       tex(uni-204.def) = %{tl_version}, tex(uni-205.def) = %{tl_version}
Provides:       tex(uni-206.def) = %{tl_version}, tex(uni-207.def) = %{tl_version}
Provides:       tex(uni-208.def) = %{tl_version}, tex(uni-209.def) = %{tl_version}
Provides:       tex(uni-210.def) = %{tl_version}, tex(uni-211.def) = %{tl_version}
Provides:       tex(uni-212.def) = %{tl_version}, tex(uni-213.def) = %{tl_version}
Provides:       tex(uni-214.def) = %{tl_version}, tex(uni-215.def) = %{tl_version}
Provides:       tex(uni-24.def) = %{tl_version}, tex(uni-248.def) = %{tl_version}
Provides:       tex(uni-249.def) = %{tl_version}, tex(uni-250.def) = %{tl_version}
Provides:       tex(uni-251.def) = %{tl_version}, tex(uni-254.def) = %{tl_version}
Provides:       tex(uni-255.def) = %{tl_version}, tex(uni-29.def) = %{tl_version}
Provides:       tex(uni-3.def) = %{tl_version}, tex(uni-30.def) = %{tl_version}
Provides:       tex(uni-31.def) = %{tl_version}, tex(uni-32.def) = %{tl_version}
Provides:       tex(uni-33.def) = %{tl_version}, tex(uni-34.def) = %{tl_version}
Provides:       tex(uni-35.def) = %{tl_version}, tex(uni-3584.def) = %{tl_version}
Provides:       tex(uni-36.def) = %{tl_version}, tex(uni-37.def) = %{tl_version}
Provides:       tex(uni-38.def) = %{tl_version}, tex(uni-39.def) = %{tl_version}
Provides:       tex(uni-4.def) = %{tl_version}, tex(uni-40.def) = %{tl_version}
Provides:       tex(uni-42.def) = %{tl_version}, tex(uni-44.def) = %{tl_version}
Provides:       tex(uni-46.def) = %{tl_version}, tex(uni-465.def) = %{tl_version}
Provides:       tex(uni-468.def) = %{tl_version}, tex(uni-469.def) = %{tl_version}
Provides:       tex(uni-47.def) = %{tl_version}, tex(uni-470.def) = %{tl_version}
Provides:       tex(uni-471.def) = %{tl_version}, tex(uni-48.def) = %{tl_version}
Provides:       tex(uni-49.def) = %{tl_version}, tex(uni-497.def) = %{tl_version}
Provides:       tex(uni-498.def) = %{tl_version}, tex(uni-5.def) = %{tl_version}
Provides:       tex(uni-50.def) = %{tl_version}, tex(uni-51.def) = %{tl_version}
Provides:       tex(uni-760.def) = %{tl_version}, tex(uni-761.def) = %{tl_version}
Provides:       tex(uni-762.def) = %{tl_version}, tex(uni-78.def) = %{tl_version}
Provides:       tex(uni-79.def) = %{tl_version}, tex(uni-80.def) = %{tl_version}
Provides:       tex(uni-81.def) = %{tl_version}, tex(uni-82.def) = %{tl_version}
Provides:       tex(uni-83.def) = %{tl_version}, tex(uni-84.def) = %{tl_version}
Provides:       tex(uni-85.def) = %{tl_version}, tex(uni-86.def) = %{tl_version}
Provides:       tex(uni-87.def) = %{tl_version}, tex(uni-88.def) = %{tl_version}
Provides:       tex(uni-89.def) = %{tl_version}, tex(uni-9.def) = %{tl_version}
Provides:       tex(uni-90.def) = %{tl_version}, tex(uni-91.def) = %{tl_version}
Provides:       tex(uni-92.def) = %{tl_version}, tex(uni-93.def) = %{tl_version}
Provides:       tex(uni-94.def) = %{tl_version}, tex(uni-95.def) = %{tl_version}
Provides:       tex(uni-96.def) = %{tl_version}, tex(uni-97.def) = %{tl_version}
Provides:       tex(uni-98.def) = %{tl_version}, tex(uni-99.def) = %{tl_version}
Provides:       tex(uni-global.def) = %{tl_version}, tex(uninames.dat) = %{tl_version}
Provides:       tex(ucs.sty) = %{tl_version}, tex(ucsencs.def) = %{tl_version}
Provides:       tex(ucshyper.sty) = %{tl_version}, tex(ucsutils.sty) = %{tl_version}
Provides:       tex(utf8x.def) = %{tl_version}, tex(autofe.sty) = %{tl_version}
Provides:       tex(c00enc.def) = %{tl_version}, tex(c10enc.def) = %{tl_version}
Provides:       tex(c40enc.def) = %{tl_version}, tex(c42enc.def) = %{tl_version}
Provides:       tex(c61enc.def) = %{tl_version}, tex(cenccmn.tex) = %{tl_version}
Provides:       tex(cp1252.enc) = %{tl_version}, tex(ldvarial.fd) = %{tl_version}
Provides:       tex(ldvc2000.fd) = %{tl_version}, tex(ldvenc.def) = %{tl_version}
Provides:       tex(letc2000.fd) = %{tl_version}, tex(letenc.def) = %{tl_version}
Provides:       tex(letgfzem.fd) = %{tl_version}, tex(letjiret.fd) = %{tl_version}
Provides:       tex(lklenc.def) = %{tl_version}, tex(lklkli.fd) = %{tl_version}
Provides:       tex(ltaarial.fd) = %{tl_version}, tex(ltac2000.fd) = %{tl_version}
Provides:       tex(ltaenc.def) = %{tl_version}, tex(ltgc2000.fd) = %{tl_version}
Provides:       tex(ltgenc.def) = %{tl_version}, tex(ltlcmr.fd) = %{tl_version}
Provides:       tex(ltlenc.def) = %{tl_version}, tex(ltwdsnol.fd) = %{tl_version}
Provides:       tex(ltwdsque.fd) = %{tl_version}, tex(ltwdssin.fd) = %{tl_version}
Provides:       tex(ltwenc.def) = %{tl_version}, tex(lucarial.fd) = %{tl_version}
Provides:       tex(lucc2000.fd) = %{tl_version}, tex(lucenc.def) = %{tl_version}
Provides:       tex(mkrenc.def) = %{tl_version}, tex(mkrezra.fd) = %{tl_version}
Provides:       tex(mkrhadas.fd) = %{tl_version}, tex(mkromega.fd) = %{tl_version}
Provides:       tex(mkrrashi.fd) = %{tl_version}, tex(t2dcmr.fd) = %{tl_version}
Provides:       tex(t2denc.def) = %{tl_version}, tex(tengwarDS.enc) = %{tl_version}
Provides:       tex(xscmr.fd) = %{tl_version}, tex(xsenc.def) = %{tl_version}

%description -n texlive-ucs
The bundle provides the ucs package, and utf8x.def, together
with a large number of support files. The utf8x.def definition
file for use with inputenc covers a wider range of Unicode
characters than does utf8.def in the LaTeX distribution. The
package provides facilities for efficient use of its large sets
of Unicode characters. Glyph production may be controlled by
various options, which permits use of non-ASCII characters when
coding mathematical formulae. Note that the bundle previously
had an alias "unicode"; that alias has now been withdrawn, and
no package of that name now exists.

%package -n texlive-ucs-doc
Summary:        Documentation for ucs
Version:        svn35853.2.2

Provides:       tex-ucs-doc
AutoReqProv:    No

%description -n texlive-ucs-doc
Documentation for ucs

%package -n texlive-uebungsblatt
Provides:       tex-uebungsblatt = %{tl_version}
License:        LPPL
Summary:        A LaTeX class for writing exercise sheets
Version:        svn15878.1.5.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(akkgerman.sty), tex(amsmath.sty), tex(inputenc.sty)
Requires:       tex(fancyhdr.sty), tex(akkcounterlabelpattern.sty)
Provides:       tex(uebungsblatt.cls) = %{tl_version}, tex(uebungsblatt.sty) = %{tl_version}

%description -n texlive-uebungsblatt
This package implements a LaTeX class for writing exercise
sheets for a lecture. Features: - quick typesetting of exercise
sheets or their revisions, - simple user friendly commands, -
elegant page formatting, - automatic numbering of exercises and
sub-exercises, - the number of the exercise sheet is extracted
automatically from the file name, - static information about
the lectures and the authors needs to provided at one point
only.

%package -n texlive-uebungsblatt-doc
Summary:        Documentation for uebungsblatt
Version:        svn15878.1.5.0

Provides:       tex-uebungsblatt-doc
AutoReqProv:    No

%description -n texlive-uebungsblatt-doc
Documentation for uebungsblatt

%package -n texlive-umoline
Provides:       tex-umoline = %{tl_version}
License:        LPPL
Summary:        Underline text allowing line breaking
Version:        svn19085.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(umoline.sty) = %{tl_version}

%description -n texlive-umoline
Provides commands \Underline, \Midline and \Overline for
underlining, striking out, and overlining their text arguments.

%package -n texlive-umoline-doc
Summary:        Documentation for umoline
Version:        svn19085.0

Provides:       tex-umoline-doc
AutoReqProv:    No

%description -n texlive-umoline-doc
Documentation for umoline

%package -n texlive-uhhassignment
Summary:        A document class for typesetting homework assignments
Version:        svn44026
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(uhhassignment.cls) = %{tl_version}

%description -n texlive-uhhassignment
This document class was created for typesetting solutions to
homework assignments at the university of Hamburg (Universitat
Hamburg).

%package -n texlive-undergradmath-doc
Summary:        LaTeX Math for Undergraduates cheat sheet
Version:        svn42926
License:        CC-BY-SA

%description -n texlive-undergradmath-doc
This is a cheat sheet for writing mathematics with LaTeX. It is
aimed at US undergraduates.

%package -n texlive-unfonts-core
Summary:        TrueType version of Un-fonts
Version:        svn44467
License:        GPLv2
Requires:       texlive-base texlive-kpathsea
Provides:       tex(UnBatang.ttf) = %{tl_version}, tex(UnBatangBold.ttf) = %{tl_version}
Provides:       tex(UnDinaru.ttf) = %{tl_version}, tex(UnDinaruBold.ttf) = %{tl_version}
Provides:       tex(UnDinaruLight.ttf) = %{tl_version}, tex(UnDotum.ttf) = %{tl_version}
Provides:       tex(UnDotumBold.ttf) = %{tl_version}, tex(UnGraphic.ttf) = %{tl_version}
Provides:       tex(UnGraphicBold.ttf) = %{tl_version}, tex(UnGungseo.ttf) = %{tl_version}
Provides:       tex(UnPilgi.ttf) = %{tl_version}, tex(UnPilgiBold.ttf) = %{tl_version}

%description -n texlive-unfonts-core
The Un-fonts come from the HLaTeX as type1 fonts in 1998 by
Koaunghi Un, he made type1 fonts to use with Korean TeX
(HLaTeX) in the late 1990's and released it under the GPL
license. They were converted to TrueType with the FontForge
(PfaEdit) by Won-kyu Park in 2003. Core families (9 fonts):
UnBatang, UnBatangBold: serif UnDotum, UnDotumBold: sans-serif
UnGraphic, UnGraphicBold: sans-serif style UnPilgi,
UnPilgiBold: script UnGungseo: cursive, brush-stroke

%package -n texlive-unfonts-extra
Summary:        TrueType version of Un-fonts
Version:        svn44465
License:        GPLv2
Requires:       texlive-base texlive-kpathsea
Provides:       tex(UnJamoBatang.ttf) = %{tl_version}, tex(UnJamoDotum.ttf) = %{tl_version}
Provides:       tex(UnJamoNovel.ttf) = %{tl_version}, tex(UnJamoSora.ttf) = %{tl_version}
Provides:       tex(UnPen.ttf) = %{tl_version}, tex(UnPenheulim.ttf) = %{tl_version}
Provides:       tex(UnPilgia.ttf) = %{tl_version}, tex(UnShinmun.ttf) = %{tl_version}
Provides:       tex(UnTaza.ttf) = %{tl_version}, tex(UnVada.ttf) = %{tl_version}
Provides:       tex(UnYetgul.ttf) = %{tl_version}

%description -n texlive-unfonts-extra
The Un-fonts come from the HLaTeX as type1 fonts in 1998 by
Koaunghi Un, he made type1 fonts to use with Korean TeX
(HLaTeX) in the late 1990's and released it under the GPL
license. They were converted to TrueType with the FontForge
(PfaEdit) by Won-kyu Park in 2003. Extra families (10 fonts):
UnPen, UnPenheulim: script UnTaza: typewriter style UnBom:
decorative UnShinmun UnYetgul: old Korean printing style
UnJamoSora, UnJamoNovel, UnJamoDotum, UnJamoBatang

%package -n texlive-unicode-bidi
Summary:        Experimental unicode bidi package for XeTeX
Version:        svn42482
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(unicode-bidi.sty) = %{tl_version}

%description -n texlive-unicode-bidi
The experimental unicode-bidi package allows to mix non-RTL
script with RTL script without any markup.

%package -n texlive-unicode-math
Provides:       tex-unicode-math = %{tl_version}
License:        LPPL 1.3
Summary:        Unicode mathematics support for XeTeX and LuaTeX
Version:        svn48309
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-fontspec, tex(luaotfload.sty), tex(lualatex-math.sty), tex(expl3.sty)
Requires:       tex(ucharcat.sty), tex(xparse.sty), tex(l3keys2e.sty), tex(fontspec.sty)
Requires:       tex(catchfile.sty), tex(fix-cm.sty), tex(filehook.sty)
Provides:       tex(unicode-math-luatex.sty) = %{tl_version}
Provides:       tex(unicode-math-table.tex) = %{tl_version}
Provides:       tex(unicode-math-xetex.sty) = %{tl_version}
Provides:       tex(unicode-math.sty) = %{tl_version}

%description -n texlive-unicode-math
This package will provide a complete implementation of unicode
maths for XeLaTeX and LuaLaTeX. Unicode maths is currently
supported by the following fonts: Cambria Math (Microsoft),
Minion Math (Johannes Kuster, typoma GmbH) Latin Modern Math
(Boguslaw Jackowski, Janusz M. Nowacki) TeX Gyre Pagella Math
(Boguslaw Jackowski, Janusz M. Nowacki) Asana-Math fonts
(Apostolos Syropolous), Neo Euler (Khaled Hosny), STIX (STI
Pub), and XITS Math (Khaled Hosny). As well as running XeTeX or
LuaTeX, this package requires recent versions of the fontspec,
expl3, xpackages, filehook, ucharcat and lualatex-math
packages.

%package -n texlive-unicode-math-doc
Summary:        Documentation for unicode-math
Version:        svn48309
Provides:       tex-unicode-math-doc
AutoReqProv:    No
Requires:       tex-fontspec-doc

%description -n texlive-unicode-math-doc
Documentation for unicode-math

%package -n texlive-venn
Provides:       tex-venn = %{tl_version}
License:        LPPL
Summary:        Creating Venn diagrams with MetaPost
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-venn
MetaPost macros for venn diagrams.

%package -n texlive-venn-doc
Summary:        Documentation for venn
Version:        svn15878.0

Provides:       tex-venn-doc
AutoReqProv:    No

%description -n texlive-venn-doc
Documentation for venn

%package -n texlive-venndiagram
Provides:       tex-venndiagram = %{tl_version}
License:        LPPL
Summary:        Creating Venn diagrams with TikZ
Version:        svn47952
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xkeyval.sty), tex(tikz.sty), tex(etoolbox.sty)
Provides:       tex(venndiagram.sty) = %{tl_version}

%description -n texlive-venndiagram
The package assists generation of simple two- and three-set
Venn diagrams for lectures or assignment sheets. The package
requires the TikZ package.

%package -n texlive-venndiagram-doc
Summary:        Documentation for venndiagram
Version:        svn47952
Provides:       tex-venndiagram-doc
AutoReqProv:    No

%description -n texlive-venndiagram-doc
Documentation for venndiagram

%package -n texlive-unitn-bimrep
Summary:        A bimonthly report class for the PhD School of Materials, Mechatronics and System Engineering
Version:        svn45581
License:        MIT
Requires:       texlive-base texlive-kpathsea
Provides:       tex(unitn-bimrep.cls) = %{tl_version}

%description -n texlive-unitn-bimrep
This package allows to rapidly write the bimonthly report for
The Ph.D. School in Materials, Mechatronics and System
Engineering. It allows to define the research activities, the
participation to school and congress, and the publication
performed by a student.

%package -n texlive-upzhkinsoku
Summary:        Supplementary Chinese kinsoku for Unicode *pTeX
Version:        svn47354
License:        Knuth
Requires:       texlive-base texlive-kpathsea
Provides:       tex(upzhkinsoku.sty) = %{tl_version}

%description -n texlive-upzhkinsoku
This package provides supplementary Chinese kinsoku (line
breaking rules etc.) settings for Unicode (e-)upTeX (when using
Unicode as its internal encoding), and ApTeX. Both LaTeX and
plain TeX are supported.

%package -n texlive-uspace
Summary:        Giving meaning to various Unicode space characters
Version:        svn42456
License:        MIT
Requires:       texlive-base texlive-kpathsea
Provides:       tex(uspace.sty) = %{tl_version}

%description -n texlive-uspace
LaTeX package that gives meaning to various Unicode space
characters.

%package -n texlive-variablelm
Summary:        Font definitions for the variable Latin Modern fonts
Version:        svn46611
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(variablelm.sty) = %{tl_version}, tex(omlvlmm.fd) = %{tl_version}
Provides:       tex(omlvlmr.fd) = %{tl_version}, tex(omsvlmr.fd) = %{tl_version}
Provides:       tex(omsvlmsy.fd) = %{tl_version}, tex(omxvlmex.fd) = %{tl_version}
Provides:       tex(ot1vlmr.fd) = %{tl_version}, tex(ot1vlmtt.fd) = %{tl_version}
Provides:       tex(t1vlmr.fd) = %{tl_version}, tex(t1vlmss.fd) = %{tl_version}
Provides:       tex(t1vlmssq.fd) = %{tl_version}, tex(t1vlmtt.fd) = %{tl_version}
Provides:       tex(t1vlmvtt.fd) = %{tl_version}, tex(ts1vlmr.fd) = %{tl_version}

%description -n texlive-variablelm
This package provides a mechanism for scaling the typeface. It
is directed to Latin Modern fonts and provides the font
definitions and the corresponding style file. This mechanism is
useful in mixed text compositions, for example Japanese-Latin.

%package -n texlive-variations
Provides:       tex-variations = %{tl_version}
License:        GPL+
Summary:        Typeset tables of variations of functions
Version:        svn15878.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(variations.sty) = %{tl_version}, tex(variations.tex) = %{tl_version}

%description -n texlive-variations
The package provides macros for typesetting tables showing
variations of functions according to French usage. These macros
may be used by both LaTeX and plain TeX users.

%package -n texlive-variations-doc
Summary:        Documentation for variations
Version:        svn15878.0.3

Provides:       tex-variations-doc
AutoReqProv:    No

%description -n texlive-variations-doc
Documentation for variations

%package -n texlive-wallcalendar
Summary:        A wall calendar class with custom layouts
Version:        svn45568
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(wallcalendar-czech.tex) = %{tl_version}
Provides:       tex(wallcalendar-dutch.tex) = %{tl_version}
Provides:       tex(wallcalendar-english.tex) = %{tl_version}
Provides:       tex(wallcalendar-french.tex) = %{tl_version}
Provides:       tex(wallcalendar-german.tex) = %{tl_version}
Provides:       tex(wallcalendar-hungarian.tex) = %{tl_version}
Provides:       tex(wallcalendar-italian.tex) = %{tl_version}
Provides:       tex(wallcalendar-japanese.tex) = %{tl_version}
Provides:       tex(wallcalendar-norwegian.tex) = %{tl_version}
Provides:       tex(wallcalendar-portuguese.tex) = %{tl_version}
Provides:       tex(wallcalendar-romanian.tex) = %{tl_version}
Provides:       tex(wallcalendar-serbian.tex) = %{tl_version}
Provides:       tex(wallcalendar-slovakian.tex) = %{tl_version}
Provides:       tex(wallcalendar-slovenian.tex) = %{tl_version}
Provides:       tex(wallcalendar-spanish.tex) = %{tl_version}
Provides:       tex(wallcalendar-swedish.tex) = %{tl_version}
Provides:       tex(wallcalendar-thai.tex) = %{tl_version}
Provides:       tex(wallcalendar.cls) = %{tl_version}

%description -n texlive-wallcalendar
This package provides a wall calendar class with custom layouts
and support for internationalization. It comes with the
following layouts: Full page photo, the calendar days overlaid
with opacity Full page photo, the photo above the calendar days
Small landscape photo, with a calendar grid Year planner
Thumbnails and captions Varnish mask There is also support for
loading event marks from a CSV file.

%package -n texlive-wtref
Summary:        Extend LaTeX's cross-reference system
Version:        svn42981
License:        MIT
Requires:       texlive-base texlive-kpathsea
Provides:       tex(wtref.sty) = %{tl_version}

%description -n texlive-wtref
This package extends the cross-reference system of LaTeX2e and
introduces concepts of namespace and scope. It also allows
users to customize reference formats. The package is part of
the WT Series.

%package -n texlive-underlin
Provides:       tex-underlin = %{tl_version}
License:        LPPL
Summary:        Underlined running heads
Version:        svn15878.1.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(underlin.sty) = %{tl_version}

%description -n texlive-underlin
Defines two pagestyles that provide underlined page heads in
LaTeX.

%package -n texlive-underlin-doc
Summary:        Documentation for underlin
Version:        svn15878.1.01

Provides:       tex-underlin-doc
AutoReqProv:    No

%description -n texlive-underlin-doc
Documentation for underlin

%package -n texlive-underoverlap
Provides:       tex-underoverlap = %{tl_version}
License:        LPPL 1.3
Summary:        Position decorations over and under expressions
Version:        svn29019.0.0.1_r1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etoolbox.sty), tex(mathtools.sty), tex(xparse.sty)
Provides:       tex(underoverlap.sty) = %{tl_version}

%description -n texlive-underoverlap
The package overcomes TeX's inherent limitations in commands
that place decorations (such as braces) at arbirary positions
over and under expressions, overlapping as necessary.

%package -n texlive-underoverlap-doc
Summary:        Documentation for underoverlap
Version:        svn29019.0.0.1_r1

Provides:       tex-underoverlap-doc
AutoReqProv:    No

%description -n texlive-underoverlap-doc
Documentation for underoverlap

%package -n texlive-undolabl
Provides:       tex-undolabl = %{tl_version}
License:        LPPL 1.3
Summary:        Override existing labels
Version:        svn36681.1.0l

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(undolabl.sty) = %{tl_version}

%description -n texlive-undolabl
The package allows the user to override existing labels (for
example, those generated automatically).

%package -n texlive-undolabl-doc
Summary:        Documentation for undolabl
Version:        svn36681.1.0l

Provides:       tex-undolabl-doc
AutoReqProv:    No

%description -n texlive-undolabl-doc
Documentation for undolabl

%package -n texlive-units
Provides:       tex-units = %{tl_version}
License:        GPL+
Summary:        Typeset units
Version:        svn42428
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty)
Provides:       tex(nicefrac.sty) = %{tl_version}, tex(units.sty) = %{tl_version}

%description -n texlive-units
The package is provided as a bundle with the nicefrac package
for typing fractions. Units uses nicefrac in typesetting
physical units in a standard-looking sort of way.

%package -n texlive-units-doc
Summary:        Documentation for units
Version:        svn42428
Provides:       tex-units-doc
AutoReqProv:    No

%description -n texlive-units-doc
Documentation for units

%package -n texlive-unravel
Provides:       tex-unravel = %{tl_version}
License:        LPPL
Summary:        Watching TeX digest tokens
Version:        svn47308
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(l3str.sty), tex(gtl.sty)
Provides:       tex(unravel.sty) = %{tl_version}

%description -n texlive-unravel
The package emulates large parts of TeX's behaviour when it
chews on tokens, expanding and performing typesetting commands.
Using unravel will let you go one step at a time through some
complicated LaTeX code that you are trying to debug. It
understands a whole breadth of TeX's features, from deeply
nested expansion to box assignments, to characters, and the
proper insertion of \everypar. The unravel package requires up-
to-date l3kernel and l3experimental bundles, as well as the new
package gtl.

%package -n texlive-unravel-doc
Summary:        Documentation for unravel
Version:        svn47308
Provides:       tex-unravel-doc
AutoReqProv:    No

%description -n texlive-unravel-doc
Documentation for unravel

%package -n texlive-upmethodology
Provides:       tex-upmethodology = %{tl_version}
License:        LGPLv2+
Summary:        Writing specifications such as for UP-based methodologies
Version:        svn46037
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(upmethodology-extension.sty), tex(a4wide.sty)
Requires:       tex(upmethodology-frontpage.sty), tex(upmethodology-spec.sty)
Requires:       tex(url.sty), tex(hyperref.sty), tex(babel.sty), tex(vmargin.sty)
Requires:       tex(upmethodology-version.sty), tex(draftwatermark.sty)
Requires:       tex(graphicx.sty), tex(subfigure.sty), tex(tabularx.sty), tex(multicol.sty)
Requires:       tex(colortbl.sty), tex(picinpar.sty), tex(amsmath.sty), tex(amsthm.sty)
Requires:       tex(thmtools.sty), tex(pifont.sty), tex(setspace.sty), tex(varioref.sty)
Requires:       tex(txfonts.sty), tex(relsize.sty), tex(xkeyval.sty), tex(hyphenat.sty)
Requires:       tex(bbm.sty), tex(environ.sty), tex(ifthen.sty), tex(xspace.sty)
Requires:       tex(xcolor.sty), tex(ifpdf.sty), tex(ulem.sty)
Provides:       tex(UPMVERSION.def) = %{tl_version}, tex(upmethodology-backpage.sty) = %{tl_version}
Provides:       tex(upmethodology-code.sty) = %{tl_version}
Provides:       tex(upmethodology-document.cls) = %{tl_version}
Provides:       tex(upmethodology-document.sty) = %{tl_version}
Provides:       tex(upmethodology-extension.sty) = %{tl_version}
Provides:       tex(upmethodology-fmt.sty) = %{tl_version}
Provides:       tex(upmethodology-frontpage.sty) = %{tl_version}
Provides:       tex(upmethodology-p-common.sty) = %{tl_version}
Provides:       tex(upmethodology-spec.sty) = %{tl_version}
Provides:       tex(upmethodology-task.sty) = %{tl_version}
Provides:       tex(upmethodology-version.sty) = %{tl_version}

%description -n texlive-upmethodology
The bundle allows the user to create Unified Process
methodology (UP or RUP) based documents. The style provides
document versioning, document history, document authors,
document validators, specification description, task
management, and several helping macros.

%package -n texlive-upmethodology-doc
Summary:        Documentation for upmethodology
Version:        svn46037
Provides:       tex-upmethodology-doc
AutoReqProv:    No

%description -n texlive-upmethodology-doc
Documentation for upmethodology

%package -n texlive-upquote
Provides:       tex-upquote = %{tl_version}
License:        LPPL 1.2
Summary:        Show "realistic" quotes in verbatim
Version:        svn26059.v1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(textcomp.sty)
Provides:       tex(upquote.sty) = %{tl_version}

%description -n texlive-upquote
Typewriter-style fonts are best for program listings, but
Computer Modern Typewriter prints ` and ' as bent opening and
closing single quotes. Other fonts, and most programming
languages, print ` as a grave accent and ' upright; ' is used
both to open and to close quoted strings. The package switches
the typewriter font to Computer Modern Typewriter in OT1
encoding, and modifies the behaviour of verbatim, verbatim*,
\verb, and \verb* to print in the "` and ' way". It does
thisregardless of other fonts or encodings in use, so long as
the package is loaded after the other fonts were. The package
does not affect \tt, \texttt, etc.

%package -n texlive-upquote-doc
Summary:        Documentation for upquote
Version:        svn26059.v1.3

Provides:       tex-upquote-doc
AutoReqProv:    No

%description -n texlive-upquote-doc
Documentation for upquote

%package -n texlive-uri
Provides:       tex-uri = %{tl_version}
License:        LPPL 1.3
Summary:        Hyperlinks for a wide range of URIs
Version:        svn21608.1.0a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty), tex(url.sty)
Provides:       tex(uri.sty) = %{tl_version}

%description -n texlive-uri
The package provides automatic hyperlinks for URIs of type
arXiv, ASIN, DOI, HDL, NBN, PubMed, OID, TINY, TINY with
preview, and XMPP and provides commands \citeurl, \mailto,
\ukoeln and \uref.

%package -n texlive-uri-doc
Summary:        Documentation for uri
Version:        svn21608.1.0a

Provides:       tex-uri-doc
AutoReqProv:    No

%description -n texlive-uri-doc
Documentation for uri

%package -n texlive-ushort
Provides:       tex-ushort = %{tl_version}
License:        LPPL
Summary:        Shorter (and longer) underlines and underbars
Version:        svn32261.2.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ushort.sty) = %{tl_version}

%description -n texlive-ushort
Some engineers need underlined or twice underlined variables
for which the usual \underline is too long. This package
provides a generic command for creating underlines of various
sizes and types.

%package -n texlive-ushort-doc
Summary:        Documentation for ushort
Version:        svn32261.2.2

Provides:       tex-ushort-doc
AutoReqProv:    No

%description -n texlive-ushort-doc
Documentation for ushort

%package -n texlive-varindex
Provides:       tex-varindex = %{tl_version}
License:        LPPL
Summary:        Luxury frontend to the \index command
Version:        svn32262.2.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(toolbox.sty)
Provides:       tex(varindex.sty) = %{tl_version}

%description -n texlive-varindex
Provides a convenient front-end for the \index command. For
example, with it you can generate multiple index entries in
almost any form by a single command. The package is highly
customizable, and works with all versions of LaTeX and probably
most other TeX formats.

%package -n texlive-varindex-doc
Summary:        Documentation for varindex
Version:        svn32262.2.3

Provides:       tex-varindex-doc
AutoReqProv:    No

%description -n texlive-varindex-doc
Documentation for varindex

%package -n texlive-varsfromjobname
Provides:       tex-varsfromjobname = %{tl_version}
License:        LPPL
Summary:        Extract variables from the name of the LaTeX file
Version:        svn44154
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty)
Provides:       tex(varsfromjobname.sty) = %{tl_version}

%description -n texlive-varsfromjobname
The package allows the user to extract information from the job
name, provided that the name has been structured appropriately:
the package expects the file name to consist of a set of words
separated by hyphens.

%package -n texlive-varsfromjobname-doc
Summary:        Documentation for varsfromjobname
Version:        svn44154
Provides:       tex-varsfromjobname-doc
AutoReqProv:    No

%description -n texlive-varsfromjobname-doc
Documentation for varsfromjobname

%package -n texlive-varwidth
Provides:       tex-varwidth = %{tl_version}
License:        LPPL
Summary:        A variable-width minipage
Version:        svn24104.0.92

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(varwidth.sty) = %{tl_version}

%description -n texlive-varwidth
The varwidth environment is superficially similar to minipage,
but the specified width is just a maximum value -- the box may
get a narrower "natural" width.

%package -n texlive-varwidth-doc
Summary:        Documentation for varwidth
Version:        svn24104.0.92

Provides:       tex-varwidth-doc
AutoReqProv:    No

%description -n texlive-varwidth-doc
Documentation for varwidth

%package -n texlive-vaucanson-g
Provides:       tex-vaucanson-g = %{tl_version}
License:        LPPL
Summary:        PSTricks macros for drawing automata
Version:        svn15878.0.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(xcolor.sty), tex(pstricks.sty), tex(pst-node.sty)
Requires:       tex(pst-plot.sty), tex(pst-coil.sty), tex(multido.sty), tex(pst-3d.sty)
Requires:       tex(calc.sty)
Provides:       tex(VCColor-names.def) = %{tl_version}, tex(VCPref-beamer.tex) = %{tl_version}
Provides:       tex(VCPref-default.tex) = %{tl_version}, tex(VCPref-mystyle.tex) = %{tl_version}
Provides:       tex(VCPref-slides.tex) = %{tl_version}, tex(Vaucanson-G.tex) = %{tl_version}
Provides:       tex(vaucanson-g.sty) = %{tl_version}, tex(vaucanson.sty) = %{tl_version}

%description -n texlive-vaucanson-g
VauCanSon-G is a package that enables the user to draw automata
within texts written using LaTeX. The package macros make use
of commands of PStricks

%package -n texlive-vaucanson-g-doc
Summary:        Documentation for vaucanson-g
Version:        svn15878.0.4

Provides:       tex-vaucanson-g-doc
AutoReqProv:    No

%description -n texlive-vaucanson-g-doc
Documentation for vaucanson-g

%package -n texlive-vocaltract
Provides:       tex-vocaltract = %{tl_version}
License:        LPPL
Summary:        Visualise the vocal tract using LaTeX and PStricks
Version:        svn25629.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(VocalTract.sty) = %{tl_version}

%description -n texlive-vocaltract
The package enables the user to visualise the vocal tract. The
vocal tract (in the package) is manipulated by a vector of
articulation parameters according to the S. Maeda model.
Animation may be achieved by providing a sequence of vectors
over time (e.g., from Matlab). A sequence of vectors for
certain German phonemes is embedded in the package, which
allows for animation when no other vector is available. The
package's graphics are produced using pstricks.

%package -n texlive-vocaltract-doc
Summary:        Documentation for vocaltract
Version:        svn25629.1

Provides:       tex-vocaltract-doc
AutoReqProv:    No

%description -n texlive-vocaltract-doc
Documentation for vocaltract

%package -n texlive-vdmlisting
Provides:       tex-vdmlisting = %{tl_version}
License:        LPPL
Summary:        Typesetting VDM in ASCII syntax
Version:        svn29944.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(listings.sty), tex(times.sty), tex(color.sty)
Provides:       tex(vdmlisting.sty) = %{tl_version}

%description -n texlive-vdmlisting
The package is an extension for the listings package that
provides a source code printer for LaTeX. This package defines
new language definitions and listing environments for the three
language dialects of the Vienna Development Method: VDM-SL, VDM-
PP and VDM-RT. If one wants to typeset VDM with a mathematical
syntax instead of the ASCII syntax used here one should use the
vdm pacakge instead

%package -n texlive-vdmlisting-doc
Summary:        Documentation for vdmlisting
Version:        svn29944.1.0

Provides:       tex-vdmlisting-doc
AutoReqProv:    No

%description -n texlive-vdmlisting-doc
Documentation for vdmlisting

%package -n texlive-verbasef
Provides:       tex-verbasef = %{tl_version}
License:        GPL+
Summary:        VERBatim Automatic Splitting of External Files
Version:        svn21922.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(vrbexin.sty), tex(verbatim.sty), tex(here.sty)
Provides:       tex(verbasef.sty) = %{tl_version}

%description -n texlive-verbasef
The package allows you to input (subsections of a) file, print
them in verbatim mode, while automatically breaking up the
input lines into pieces of a given length, which are output as
figures. These figures are posted using the [H] specification,
which forces LaTeX to place the figure at the spot of
invocation, rather than floating the figures to the top of the
next page. The package requires the verbatim, here and vrbexin
packages.

%package -n texlive-verbasef-doc
Summary:        Documentation for verbasef
Version:        svn21922.1.1

Provides:       tex-verbasef-doc
AutoReqProv:    No

%description -n texlive-verbasef-doc
Documentation for verbasef

%package -n texlive-varisize
Provides:       tex-varisize = %{tl_version}
License:        Public Domain
Summary:        Change font size in Plain TeX
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(10point.tex) = %{tl_version}, tex(10pointss.tex) = %{tl_version}
Provides:       tex(11point.tex) = %{tl_version}, tex(12point.tex) = %{tl_version}
Provides:       tex(14point.tex) = %{tl_version}, tex(17point.tex) = %{tl_version}
Provides:       tex(20point.tex) = %{tl_version}, tex(7point.tex) = %{tl_version}
Provides:       tex(8point.tex) = %{tl_version}, tex(9point.tex) = %{tl_version}

%description -n texlive-varisize
A series of files, each of which defines a size-change macro.
Note that 10point.tex is by convention called by one of the
other files, so that there's always a "way back".

%package -n texlive-varisize-doc
Summary:        Documentation for varisize
Version:        svn15878.0

Provides:       tex-varisize-doc
AutoReqProv:    No

%description -n texlive-varisize-doc
Documentation for varisize

%package -n texlive-verbatimbox
Provides:       tex-verbatimbox = %{tl_version}
License:        LPPL
Summary:        Deposit verbatim text in a box
Version:        svn33197.3.13

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(readarray.sty), tex(ifnextok.sty), tex(verbatim.sty)
Provides:       tex(verbatimbox.sty) = %{tl_version}

%description -n texlive-verbatimbox
The package provides a verbbox environment (which uses
techniques similar to those of the boxedverbatim environment of
the moreverb package) to place its contents into a globally
available box, or into a box specified by the user. The global
box may then be used in a variety of situations (for example,
providing a replica of the boxedverbatim environment itself). A
valuable use is in places where the standard verbatim
environment (which is based on a trivlist) may not appear. The
package makes use of the verbatim package (which is a required
part of any LaTeX distribution).

%package -n texlive-verbatimbox-doc
Summary:        Documentation for verbatimbox
Version:        svn33197.3.13

Provides:       tex-verbatimbox-doc
AutoReqProv:    No

%description -n texlive-verbatimbox-doc
Documentation for verbatimbox

%package -n texlive-verbatimcopy
Provides:       tex-verbatimcopy = %{tl_version}
License:        LPPL
Summary:        Make copies of text documents from within LaTeX
Version:        svn15878.0.06

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(verbatim.sty)
Provides:       tex(verbatimcopy.sty) = %{tl_version}

%description -n texlive-verbatimcopy
This package provides \VerbatimCopy{in}{out} that will enable
LaTeX to take a verbatim copy of one text file, and save it
under another name. The package provides a means to specify the
output directory to be used, but does no checking and may
therefore overwrite an important file if used injudiciously.

%package -n texlive-verbatimcopy-doc
Summary:        Documentation for verbatimcopy
Version:        svn15878.0.06

Provides:       tex-verbatimcopy-doc
AutoReqProv:    No

%description -n texlive-verbatimcopy-doc
Documentation for verbatimcopy

%package -n texlive-verbdef
Provides:       tex-verbdef = %{tl_version}
License:        LPPL
Summary:        Define commands which expand to verbatim text
Version:        svn17177.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(verbdef.sty) = %{tl_version}

%description -n texlive-verbdef
The package defines a single command \verbdef (which has a *-
form, like \verb). \verbdef will define a robust command whose
body expands to verbatim text. By using commands defined by
\verbdef, one can put verbatim text into the arguments of
commands; since the defined command is robust, it doesn't
matter if the argument is moving. (Full details of syntax and
caveats about use are in comments in the file itself.)

%package -n texlive-verbdef-doc
Summary:        Documentation for verbdef
Version:        svn17177.0.2

Provides:       tex-verbdef-doc
AutoReqProv:    No

%description -n texlive-verbdef-doc
Documentation for verbdef

%package -n texlive-verbments
Provides:       tex-verbments = %{tl_version}
License:        LPPL 1.2
Summary:        Syntax highlighting of source code in LaTeX documents
Version:        svn23670.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty), tex(fancyvrb.sty), tex(framed.sty), tex(xcolor.sty)
Requires:       tex(calc.sty)
Provides:       tex(verbments.sty) = %{tl_version}

%description -n texlive-verbments
The package provides an environment for syntax highlighting
source code in LaTeX documents. The highlighted source code
output is formatted via powerful Pygments library of the Python
language.

%package -n texlive-verbments-doc
Summary:        Documentation for verbments
Version:        svn23670.1.2

Provides:       tex-verbments-doc
AutoReqProv:    No

%description -n texlive-verbments-doc
Documentation for verbments

%package -n texlive-verse
Provides:       tex-verse = %{tl_version}
License:        LPPL
Summary:        Aids for typesetting simple verse
Version:        svn34017.2.4b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(verse.sty) = %{tl_version}

%description -n texlive-verse
The package documentation discusses approaches to the problem;
the package is strong on layout, from simple alternate-line
indentation to the Mouse's tale from Alice in Wonderland.

%package -n texlive-verse-doc
Summary:        Documentation for verse
Version:        svn34017.2.4b

Provides:       tex-verse-doc
AutoReqProv:    No

%description -n texlive-verse-doc
Documentation for verse

%package -n texlive-version
Provides:       tex-version = %{tl_version}
License:        Copyright only
Summary:        Conditionally include text
Version:        svn21920.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(version.sty) = %{tl_version}

%description -n texlive-version
Defines macros \includeversion{NAME} and \excludeversion{NAME},
each of which defines an environment NAME whose text is to be
included or excluded from compilation. Although the command
syntax is very similar to that of comment, comment.sty is to be
preferred to version.sty for documents where significant chunks
of text may be excluded.

%package -n texlive-version-doc
Summary:        Documentation for version
Version:        svn21920.2.0

Provides:       tex-version-doc
AutoReqProv:    No

%description -n texlive-version-doc
Documentation for version

%package -n texlive-versions
Provides:       tex-versions = %{tl_version}
License:        LPPL 1.3
Summary:        Optionally omit pieces of text
Version:        svn21921.0.55

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(versions.sty) = %{tl_version}

%description -n texlive-versions
Stephan Bellantoni's version has provided preamble commands for
selecting environments to be included/excluded. This package
does the same, but corrects, improves, and extends it in both
implementation and function.

%package -n texlive-versions-doc
Summary:        Documentation for versions
Version:        svn21921.0.55

Provides:       tex-versions-doc
AutoReqProv:    No

%description -n texlive-versions-doc
Documentation for versions

%package -n texlive-versonotes
Provides:       tex-versonotes = %{tl_version}
License:        LPPL 1.3
Summary:        Display brief notes on verso pages
Version:        svn39084

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(versonotes.sty) = %{tl_version}

%description -n texlive-versonotes
This package allows you to place notes on the verso pages of an
otherwise single-sided document. If, in the run of text, you
include a call to the macro \versonote{This is a remark}, then
that text will be placed on the opposite (ie, 'verso') page,
lined up with the macro call.

%package -n texlive-versonotes-doc
Summary:        Documentation for versonotes
Version:        svn39084

Provides:       tex-versonotes-doc
AutoReqProv:    No

%description -n texlive-versonotes-doc
Documentation for versonotes

%package -n texlive-vertbars
Provides:       tex-vertbars = %{tl_version}
License:        LPPL 1.3
Summary:        Mark vertical rules in margin of text
Version:        svn20589.1.0b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(lineno.sty)
Provides:       tex(vertbars.sty) = %{tl_version}

%description -n texlive-vertbars
This package is an extension to lineno, replacing that
package's line numbers with bars to the left or right of the
text.

%package -n texlive-vertbars-doc
Summary:        Documentation for vertbars
Version:        svn20589.1.0b

Provides:       tex-vertbars-doc
AutoReqProv:    No

%description -n texlive-vertbars-doc
Documentation for vertbars

%package -n texlive-vgrid
Provides:       tex-vgrid = %{tl_version}
License:        LPPL 1.3
Summary:        Overlay a grid on the printed page
Version:        svn32457.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(everypage.sty), tex(tikz.sty), tex(ifoddpage.sty)
Provides:       tex(vgrid.sty) = %{tl_version}

%description -n texlive-vgrid
The package overlays a grid (whose spacing is \baselineskip,
which offers guidlines for considering the "rhythm" of the
document on the page.

%package -n texlive-vgrid-doc
Summary:        Documentation for vgrid
Version:        svn32457.0.1

Provides:       tex-vgrid-doc
AutoReqProv:    No

%description -n texlive-vgrid-doc
Documentation for vgrid

%package -n texlive-vhistory
Provides:       tex-vhistory = %{tl_version}
License:        LPPL 1.2
Summary:        Support for creating a change log
Version:        svn30080.1.6.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ltxtable.sty)
Provides:       tex(sets.sty) = %{tl_version}, tex(vhistory.sty) = %{tl_version}

%description -n texlive-vhistory
Vhistory simplifies the creation of a history of versions of a
document. You can easily extract information like the current
version of a list of authors from that history. It helps you to
get consistent documents. The package sets, which is used by
vhistory, allows you to use sets containing text. You can use
the usual operations to create the union of sets or the
intersection of sets etc.

%package -n texlive-vhistory-doc
Summary:        Documentation for vhistory
Version:        svn30080.1.6.1

Provides:       tex-vhistory-doc
AutoReqProv:    No

%description -n texlive-vhistory-doc
Documentation for vhistory

%package -n texlive-vmargin
Provides:       tex-vmargin = %{tl_version}
License:        LPPL
Summary:        Set various page dimensions
Version:        svn15878.2.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(vmargin.sty) = %{tl_version}

%description -n texlive-vmargin
Provides a macro to set various margins as well as dimensions
for header/footer and page dimensions. Most common paper sizes,
paper orientation, disabling of headers and footers, and two
sided printing are supported. The vmargin package does not rely
on other packages and was designed with speed and size in mind.
Its user interface might not be very fancy, but it's fast,
small, and gets the job done. If you are looking for something
more elaborate try the geometry package.

%package -n texlive-vmargin-doc
Summary:        Documentation for vmargin
Version:        svn15878.2.5

Provides:       tex-vmargin-doc
AutoReqProv:    No

%description -n texlive-vmargin-doc
Documentation for vmargin

%package -n texlive-volumes
Provides:       tex-volumes = %{tl_version}
License:        LPPL
Summary:        Typeset only parts of a document, with complete indexes etc
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(scrlfile.sty)
Provides:       tex(nowtoaux.sty) = %{tl_version}, tex(volumes.sty) = %{tl_version}

%description -n texlive-volumes
This package helps you if you want to produce separate printed
volumes from one LaTeX document, as well as one comprehensive,
"all-inclusive" version. It suppresses the part of the table of
contents that are not typeset, while counters, definitions,
index entries etc. are kept consistent throughout the input
file.

%package -n texlive-volumes-doc
Summary:        Documentation for volumes
Version:        svn15878.1.0

Provides:       tex-volumes-doc
AutoReqProv:    No

%description -n texlive-volumes-doc
Documentation for volumes

%package -n texlive-vruler
Provides:       tex-vruler = %{tl_version}
License:        LPPL
Summary:        Numbering text
Version:        svn21598.2.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(vruler.sty) = %{tl_version}

%description -n texlive-vruler
The package offers facilities for adding a columns of numbering
to the general text so that the text can be properly
referenced. The vertical ruler can be scaled and moved freely.
The package may be used either with LaTeX or with plain TeX.

%package -n texlive-vruler-doc
Summary:        Documentation for vruler
Version:        svn21598.2.3

Provides:       tex-vruler-doc
AutoReqProv:    No

%description -n texlive-vruler-doc
Documentation for vruler

%package -n texlive-vwcol
Provides:       tex-vwcol = %{tl_version}
License:        LPPL 1.3
Summary:        Variable-width multiple text columns
Version:        svn36254.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty), tex(color.sty), tex(environ.sty), tex(keyval.sty)
Requires:       tex(ragged2e.sty)
Provides:       tex(vwcol.sty) = %{tl_version}

%description -n texlive-vwcol
The package provides a crude environment (vwcol) for
typesetting multicolumn paragraph text of various column widths
on a single page.

%package -n texlive-vwcol-doc
Summary:        Documentation for vwcol
Version:        svn36254.0.2

Provides:       tex-vwcol-doc
AutoReqProv:    No

%description -n texlive-vwcol-doc
Documentation for vwcol

%package -n texlive-wallpaper
Provides:       tex-wallpaper = %{tl_version}
License:        LPPL
Summary:        Easy addition of wallpapers (background images) to LaTeX documents, including tiling
Version:        svn15878.1.10

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(calc.sty), tex(eso-pic.sty), tex(graphicx.sty)
Provides:       tex(wallpaper.sty) = %{tl_version}

%description -n texlive-wallpaper
This collection contains files to add wallpapers (background
images) to LaTeX documents. It uses the eso-pic package, but
provides simple commands to include effects such as tiling. An
example is provided, which works under both LaTeX and pdfLaTeX.

%package -n texlive-wallpaper-doc
Summary:        Documentation for wallpaper
Version:        svn15878.1.10

Provides:       tex-wallpaper-doc
AutoReqProv:    No

%description -n texlive-wallpaper-doc
Documentation for wallpaper

%package -n texlive-warning
Provides:       tex-warning = %{tl_version}
License:        LPPL
Summary:        Global warnings at the end of the logfile
Version:        svn22028.0.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(warning.sty) = %{tl_version}

%description -n texlive-warning
This package provides a command that generates a list of
warnings that are printed out at the very end of the logfile.
This is useful for warnings such as 'Rerun for this or that
reason' or 'This is a draft, change it before the final run'.

%package -n texlive-warning-doc
Summary:        Documentation for warning
Version:        svn22028.0.01

Provides:       tex-warning-doc
AutoReqProv:    No

%description -n texlive-warning-doc
Documentation for warning

%package -n texlive-warpcol
Provides:       tex-warpcol = %{tl_version}
License:        LPPL
Summary:        Relative alignment of rows in numeric columns in tabulars
Version:        svn15878.1.0c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(array.sty)
Provides:       tex(warpcol.sty) = %{tl_version}

%description -n texlive-warpcol
Defines a tabular column type for formatting numerical columns
in LaTeX. The column type enables numerical items to be right
justified relative to each other, while centred beneath the
column label. In addition, macros are provided to enable
variations on this column type to be defined. Usage of the
package is superficially similar to that of dcolumn; however,
the alignment scheme is different, and the packages have
different, though overlapping, applications.

%package -n texlive-warpcol-doc
Summary:        Documentation for warpcol
Version:        svn15878.1.0c

Provides:       tex-warpcol-doc
AutoReqProv:    No

%description -n texlive-warpcol-doc
Documentation for warpcol

%package -n texlive-was
Provides:       tex-was = %{tl_version}
License:        Public Domain
Summary:        A collection of small packages by Walter Schmidt
Version:        svn21439.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(fixmath.sty) = %{tl_version}, tex(gensymb.sty) = %{tl_version}
Provides:       tex(icomma.sty) = %{tl_version}, tex(upgreek.sty) = %{tl_version}

%description -n texlive-was
A bundle of packages that arise in the author's area of
interest: compliance of maths typesetting with ISO standards;
symbols that work in both maths and text modes commas for both
decimal separator and maths; and upright Greek letters in
maths.

%package -n texlive-was-doc
Summary:        Documentation for was
Version:        svn21439.0

Provides:       tex-was-doc
AutoReqProv:    No

%description -n texlive-was-doc
Documentation for was

%package -n texlive-webguide-doc
Summary:        Documentation for webguide
Version:        svn25813.0

Provides:       tex-webguide-doc
AutoReqProv:    No

%description -n texlive-webguide-doc
Documentation for webguide

%package -n texlive-visualfaq-doc
Summary:        Documentation for visualfaq
Version:        svn38647

Provides:       tex-visualfaq-doc
AutoReqProv:    No

%description -n texlive-visualfaq-doc
Documentation for visualfaq

%package -n texlive-voss-mathcol-doc
Summary:        Documentation for voss-mathcol
Version:        svn32954.0.1

Provides:       tex-voss-mathcol-doc
AutoReqProv:    No

%description -n texlive-voss-mathcol-doc
Documentation for voss-mathcol

%package -n texlive-utf8mex
Provides:       tex-utf8mex = %{tl_version}
License:        Public Domain
Summary:        Tools to produce formats that read Polish language input
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(utf8-pl.tex) = %{tl_version}, tex(utf8plsq.tex) = %{tl_version}

%description -n texlive-utf8mex
The bundle provides files for building formats to read input in
Polish encodings.

%package -n texlive-utf8mex-doc
Summary:        Documentation for utf8mex
Version:        svn15878.0

Provides:       tex-utf8mex-doc
AutoReqProv:    No

%description -n texlive-utf8mex-doc
Documentation for utf8mex

%package -n texlive-widetable
Provides:       tex-widetable = %{tl_version}
License:        LPPL 1.3
Summary:        An environment for typesetting tables of specified width
Version:        svn45258
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifetex.sty)
Provides:       tex(widetable.sty) = %{tl_version}

%description -n texlive-widetable
The package defines a new environment that, unlike tabularX,
typesets a table of specified width by working on the inter-
column glue; the tabular cells will all be stretched (or
shrunk) according to need. The package will use the e-TeX
arithmetic extensions if they are available (they are, in most
modern distributions).

%package -n texlive-widetable-doc
Summary:        Documentation for widetable
Version:        svn45258
Provides:       tex-widetable-doc
AutoReqProv:    No

%description -n texlive-widetable-doc
Documentation for widetable

%package -n texlive-williams
Provides:       tex-williams = %{tl_version}
License:        LPPL
Summary:        Miscellaneous macros by Peter Williams
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty), tex(ifthen.sty), tex(epic.sty), tex(eepic.sty)
Provides:       tex(antree.sty) = %{tl_version}, tex(toklist.sty) = %{tl_version}

%description -n texlive-williams
The bundle provides two packages: - antree, which provides
macros for annotated node trees, and - toklist, which is an
implementation of Knuth's token list macros, to be found on
pp.378-379 of the TeXbook.

%package -n texlive-williams-doc
Summary:        Documentation for williams
Version:        svn15878.0

Provides:       tex-williams-doc
AutoReqProv:    No

%description -n texlive-williams-doc
Documentation for williams

%package -n texlive-withargs
Provides:       tex-withargs = %{tl_version}
License:        LPPL 1.3
Summary:        Ephemeral macro use
Version:        svn42756
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(filecontents.sty), tex(xparse.sty), tex(etoolbox.sty), tex(mdframed.sty)
Requires:       tex(marginnote.sty), tex(listings.sty), tex(textcomp.sty), tex(hyperref.sty)
Requires:       tex(needspace.sty), tex(noindentafter.sty)
Requires:       tex(ifthen.sty), tex(expl3.sty), tex(l3regex.sty)
Provides:       tex(withargs-dry.sty) = %{tl_version}, tex(dry.sty) = %{tl_version}
Provides:       tex(withargs-packagedoc.cls) = %{tl_version}
Provides:       tex(withargs.sty) = %{tl_version}

%description -n texlive-withargs
withargs package

%package -n texlive-withargs-doc
Summary:        Documentation for withargs
Version:        svn42756
Provides:       tex-withargs-doc
AutoReqProv:    No

%description -n texlive-withargs-doc
Documentation for withargs

%package -n texlive-wordlike
Provides:       tex-wordlike = %{tl_version}
License:        LPPL
Summary:        Simulating word processor layout
Version:        svn15878.1.2b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(geometry.sty), tex(mathptmx.sty), tex(helvet.sty), tex(courier.sty)
Provides:       tex(wordlike.sty) = %{tl_version}

%description -n texlive-wordlike
The package simulates typical word processor layout: narrow
page margins, Times, Helvetica and Courier fonts, \LARGE or
\Large headings, and \sloppy typesetting. The package aims at
making life easier for users who are discontent with LaTeX's
standard layout settings because they need a layout that
resembles the usual "wordlike" output. The design of the
package draws on several discussions in the de.comp.text.tex
and comp.text.tex newsgroups that are referred to in the
manual.

%package -n texlive-wordlike-doc
Summary:        Documentation for wordlike
Version:        svn15878.1.2b

Provides:       tex-wordlike-doc
AutoReqProv:    No

%description -n texlive-wordlike-doc
Documentation for wordlike

%package -n texlive-wrapfig
Provides:       tex-wrapfig = %{tl_version}
License:        LPPL
Summary:        Produces figures which text can flow around
Version:        svn22048.3.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(wrapfig.sty) = %{tl_version}

%description -n texlive-wrapfig
Allows figures or tables to have text wrapped around them. Does
not work in combination with list environments, but can be used
in a parbox or minipage, and in twocolumn format. Supports the
float package.

%package -n texlive-wrapfig-doc
Summary:        Documentation for wrapfig
Version:        svn22048.3.6

Provides:       tex-wrapfig-doc
AutoReqProv:    No

%description -n texlive-wrapfig-doc
Documentation for wrapfig

%package -n texlive-uaclasses
Provides:       tex-uaclasses = %{tl_version}
License:        Public Domain
Summary:        University of Arizona thesis and dissertation format
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amsmath.sty), tex(amsfonts.sty), tex(amsthm.sty)
Provides:       tex(my-thesis.cls) = %{tl_version}, tex(my-title.sty) = %{tl_version}
Provides:       tex(ua-thesis.cls) = %{tl_version}, tex(ua-title.sty) = %{tl_version}

%description -n texlive-uaclasses
This package provides a LaTeX2e document class named 'ua-
thesis' for typesetting theses and dissertations in the
official format required by the University of Arizona.
Moreover, there is a fully compatible alternative document
class 'my-thesis' for private 'nice' copies of the
dissertation, and the respective title pages are available as
separate packages to work with any document class.

%package -n texlive-uaclasses-doc
Summary:        Documentation for uaclasses
Version:        svn15878.0

Provides:       tex-uaclasses-doc
AutoReqProv:    No

%description -n texlive-uaclasses-doc
Documentation for uaclasses

%package -n texlive-uafthesis
Provides:       tex-uafthesis = %{tl_version}
License:        LPPL
Summary:        Document class for theses at University of Alaska Fairbanks
Version:        svn29349.12.12

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(uafthesis.cls) = %{tl_version}

%description -n texlive-uafthesis
This is an "unofficial" official class.

%package -n texlive-uafthesis-doc
Summary:        Documentation for uafthesis
Version:        svn29349.12.12

Provides:       tex-uafthesis-doc
AutoReqProv:    No

%description -n texlive-uafthesis-doc
Documentation for uafthesis

%package -n texlive-ucbthesis
Provides:       tex-ucbthesis = %{tl_version}
License:        LPPL 1.3
Summary:        Thesis and dissertation class supporting UCB requirements
Version:        svn37776.3.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ucbthesis.cls) = %{tl_version}

%description -n texlive-ucbthesis
The class provides the necessary framework for electronic
submission of Masters theses and Ph.D. dissertations at the
University of California, Berkeley. It is based on the memoir
class.

%package -n texlive-ucbthesis-doc
Summary:        Documentation for ucbthesis
Version:        svn37776.3.5

Provides:       tex-ucbthesis-doc
AutoReqProv:    No

%description -n texlive-ucbthesis-doc
Documentation for ucbthesis

%package -n texlive-ucdavisthesis
Provides:       tex-ucdavisthesis = %{tl_version}
License:        LPPL
Summary:        A thesis/dissertation class for University of California at Davis
Version:        svn40772

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(ucdavisthesis.cls) = %{tl_version}, tex(ucdthesis10.clo) = %{tl_version}
Provides:       tex(ucdthesis11.clo) = %{tl_version}, tex(ucdthesis12.clo) = %{tl_version}
Provides:       tex(ucdthesis13.clo) = %{tl_version}

%description -n texlive-ucdavisthesis
The class conforms to the University's requirements for 2009.

%package -n texlive-ucdavisthesis-doc
Summary:        Documentation for ucdavisthesis
Version:        svn40772

Provides:       tex-ucdavisthesis-doc
AutoReqProv:    No

%description -n texlive-ucdavisthesis-doc
Documentation for ucdavisthesis

%package -n texlive-ucthesis
Provides:       tex-ucthesis = %{tl_version}
License:        LPPL 1.3
Summary:        University of California thesis format
Version:        svn15878.3.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(uct10.clo) = %{tl_version}, tex(uct11.clo) = %{tl_version}
Provides:       tex(uct12.clo) = %{tl_version}, tex(ucthesis.cls) = %{tl_version}

%description -n texlive-ucthesis
A modified version of the standard LaTeX report style that is
accepted for use with University of California PhD
dissertations and Masters theses. A sample dissertation source
and bibliography are provided.

%package -n texlive-ucthesis-doc
Summary:        Documentation for ucthesis
Version:        svn15878.3.2

Provides:       tex-ucthesis-doc
AutoReqProv:    No

%description -n texlive-ucthesis-doc
Documentation for ucthesis

%package -n texlive-uestcthesis
Provides:       tex-uestcthesis = %{tl_version}
License:        LPPL 1.3
Summary:        Thesis class for UESTC
Version:        svn36371.1.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(mathptmx.sty), tex(etoolbox.sty), tex(ifthen.sty), tex(geometry.sty)
Requires:       tex(graphicx.sty), tex(calc.sty), tex(float.sty), tex(texnames.sty)
Requires:       tex(caption.sty), tex(booktabs.sty), tex(tabularx.sty), tex(threeparttable.sty)
Requires:       tex(longtable.sty), tex(placeins.sty), tex(flafter.sty), tex(amsmath.sty)
Requires:       tex(amsfonts.sty), tex(amssymb.sty), tex(bm.sty), tex(ntheorem.sty)
Requires:       tex(natbib.sty), tex(multibib.sty), tex(footmisc.sty), tex(pifont.sty)
Requires:       tex(cmap.sty), tex(hyperxmp.sty), tex(hyperref.sty), tex(subfigure.sty)
Requires:       tex(enumitem.sty), tex(color.sty), tex(marvosym.sty), tex(glossaries.sty)
Provides:       tex(uestcthesis.cls) = %{tl_version}

%description -n texlive-uestcthesis
The class is for typesetting a thesis at the University of
Electronic Science and Technology of China.

%package -n texlive-uestcthesis-doc
Summary:        Documentation for uestcthesis
Version:        svn36371.1.1.0

Provides:       tex-uestcthesis-doc
AutoReqProv:    No

%description -n texlive-uestcthesis-doc
Documentation for uestcthesis

%package -n texlive-uiucredborder
Provides:       tex-uiucredborder = %{tl_version}
License:        LPPL 1.2
Summary:        Class for UIUC thesis red-bordered forms
Version:        svn29974.1.00

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(geometry.sty)
Provides:       tex(uiucredborder.cls) = %{tl_version}

%description -n texlive-uiucredborder
The class offers a means of filling out the "red-bordered form"
that gets signed by the department head, your advisor, and --
for doctoral dissertations -- your thesis committee members.

%package -n texlive-uiucredborder-doc
Summary:        Documentation for uiucredborder
Version:        svn29974.1.00

Provides:       tex-uiucredborder-doc
AutoReqProv:    No

%description -n texlive-uiucredborder-doc
Documentation for uiucredborder

%package -n texlive-uiucthesis
Provides:       tex-uiucthesis = %{tl_version}
License:        LPPL
Summary:        UIUC thesis class
Version:        svn15878.2.25

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(setspace.sty)
Provides:       tex(uiucthesis.cls) = %{tl_version}, tex(uiucthesis.sty) = %{tl_version}

%description -n texlive-uiucthesis
The class produces a document that conforms to the format
described in the University's Handbook for Graduate Students
Preparing to Deposit.

%package -n texlive-uiucthesis-doc
Summary:        Documentation for uiucthesis
Version:        svn15878.2.25

Provides:       tex-uiucthesis-doc
AutoReqProv:    No

%description -n texlive-uiucthesis-doc
Documentation for uiucthesis

%package -n texlive-ulem
Provides:       tex-ulem = %{tl_version}
License:        Copyright only
Summary:        Package for underlining
Version:        svn26785.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ulem.sty) = %{tl_version}

%description -n texlive-ulem
The package provides an \ul (underline) command which will
break over line ends; this technique may be used to replace \em
(both in that form and as the \emph command), so as to make
output look as if it comes from a typewriter. The package also
offers double and wavy underlining, and striking out (line
through words) and crossing out (/// over words). The package
works with both Plain TeX and LaTeX.

%package -n texlive-ulem-doc
Summary:        Documentation for ulem
Version:        svn26785.0

Provides:       tex-ulem-doc
AutoReqProv:    No

%description -n texlive-ulem-doc
Documentation for ulem

%package -n texlive-ulthese
Provides:       tex-ulthese = %{tl_version}
License:        LPPL 1.3
Summary:        Thesis class and templates for Universite Laval
Version:        svn44456
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty), tex(ifxetex.sty), tex(fontspec.sty), tex(unicode-math.sty)
Requires:       tex(fontenc.sty), tex(natbib.sty), tex(babel.sty), tex(numprint.sty)
Requires:       tex(graphicx.sty), tex(xcolor.sty), tex(textcomp.sty)
Provides:       tex(ulthese.cls) = %{tl_version}

%description -n texlive-ulthese
The package provides a class based on memoir to prepare theses
and memoirs compliant with the presentation rules set forth by
the Faculty of Graduate Studies of Universite Laval, Quebec,
Canada. The class also comes with an extensive set of templates
for the various types of theses and memoirs offered at Laval.
Please note that the documentation for the class and the
comments in the templates are all written in French, the
language of the target audience.

%package -n texlive-ulthese-doc
Summary:        Documentation for ulthese
Version:        svn44456
Provides:       tex-ulthese-doc
AutoReqProv:    No

%description -n texlive-ulthese-doc
Documentation for ulthese

%package -n texlive-umthesis
Provides:       tex-umthesis = %{tl_version}
License:        LPPL
Summary:        Dissertations at the University of Michigan
Version:        svn15878.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(setspace.sty), tex(ifthen.sty), tex(etex.sty), tex(hyperref.sty)
Provides:       tex(umthesis.cls) = %{tl_version}

%description -n texlive-umthesis
The class loads book class, and makes minimal changes to it;
its coding aims to be as robust as possible, and as a result it
has few conflicts with potential add-on packages.

%package -n texlive-umthesis-doc
Summary:        Documentation for umthesis
Version:        svn15878.0.2

Provides:       tex-umthesis-doc
AutoReqProv:    No

%description -n texlive-umthesis-doc
Documentation for umthesis

%package -n texlive-umich-thesis
Provides:       tex-umich-thesis = %{tl_version}
License:        LPPL
Summary:        University of Michigan Thesis LaTeX class
Version:        svn15878.1.20

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(geometry.sty), tex(setspace.sty), tex(placeins.sty)
Provides:       tex(umich-thesis.cls) = %{tl_version}

%description -n texlive-umich-thesis
A LaTeX2e class to create a University of Michigan dissertation
according to the Rackham dissertation handbook.

%package -n texlive-umich-thesis-doc
Summary:        Documentation for umich-thesis
Version:        svn15878.1.20

Provides:       tex-umich-thesis-doc
AutoReqProv:    No

%description -n texlive-umich-thesis-doc
Documentation for umich-thesis

%package -n texlive-unamth-template-doc
Summary:        Documentation for unamth-template
Version:        svn33625.2.0

Provides:       tex-unamth-template-doc
AutoReqProv:    No

%description -n texlive-unamth-template-doc
Documentation for unamth-template

%package -n texlive-unamthesis
Provides:       tex-unamthesis = %{tl_version}
License:        LPPL 1.3
Summary:        Style for Universidad Nacional Autonoma de Mexico theses
Version:        svn43639
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(graphicx.sty), tex(setspace.sty)
Provides:       tex(UNAMThesis.sty) = %{tl_version}

%description -n texlive-unamthesis
The package provides a customisable format to typeset Theses
according to the Universidad Nacional Autonoma de Mexico
guidelines. Support for use in Scientific Workplace (SWP) 3.x
is also provided. The bundle also includes an appropriate
bibliographic style which enables the use of author-year
schemes using the natbib package.

%package -n texlive-unamthesis-doc
Summary:        Documentation for unamthesis
Version:        svn43639
Provides:       tex-unamthesis-doc
AutoReqProv:    No

%description -n texlive-unamthesis-doc
Documentation for unamthesis

%package -n texlive-unswcover
Provides:       tex-unswcover = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset a dissertation cover page following UNSW guidelines
Version:        svn29476.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(babel.sty), tex(graphicx.sty), tex(pdfpages.sty)
Provides:       tex(unswcover.sty) = %{tl_version}

%description -n texlive-unswcover
The package an UNSW cover sheet following the 2011 GRS
guidelines. It may also (optionally) provide other required
sheets such as Originality, Copyright and Authenticity
statements.

%package -n texlive-unswcover-doc
Summary:        Documentation for unswcover
Version:        svn29476.1.0

Provides:       tex-unswcover-doc
AutoReqProv:    No

%description -n texlive-unswcover-doc
Documentation for unswcover

%package -n texlive-uothesis
Provides:       tex-uothesis = %{tl_version}
License:        LPPL 1.3
Summary:        Class for dissertations and theses at the University of Oregon
Version:        svn25355.2.5.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(float.sty), tex(subfig.sty), tex(xcolor.sty), tex(graphicx.sty)
Requires:       tex(setspace.sty), tex(xspace.sty), tex(lineno.sty), tex(layouts.sty)
Requires:       tex(todonotes.sty), tex(ragged2e.sty), tex(mhchem.sty), tex(amsmath.sty)
Requires:       tex(amsthm.sty), tex(amssymb.sty), tex(lipsum.sty), tex(natbib.sty)
Requires:       tex(draftwatermark.sty), tex(hyperref.sty)
Provides:       tex(uothesis.cls) = %{tl_version}

%description -n texlive-uothesis
The class generates documents that are suitable for submission
to the Graduate School and conform with the style requirements
for dissertations and theses as laid out in the Fall 2010 UO
graduate school student manual.

%package -n texlive-uothesis-doc
Summary:        Documentation for uothesis
Version:        svn25355.2.5.6

Provides:       tex-uothesis-doc
AutoReqProv:    No

%description -n texlive-uothesis-doc
Documentation for uothesis

%package -n texlive-urcls
Provides:       tex-urcls = %{tl_version}
License:        LPPL
Summary:        Beamer and scrlttr2 classes and styles for the University of Regensburg
Version:        svn43734
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty), tex(graphicx.sty), tex(xcolor.sty), tex(inputenc.sty)
Requires:       tex(fontenc.sty), tex(babel.sty), tex(calc.sty), tex(tikz.sty)
Requires:       tex(pgf.sty), tex(kvoptions.sty)
Provides:       tex(URbeamer.cls) = %{tl_version}, tex(URcolors.sty) = %{tl_version}
Provides:       tex(URletter.cls) = %{tl_version}, tex(beamercolorthemeUR.sty) = %{tl_version}
Provides:       tex(beamerfontthemeUR.sty) = %{tl_version}
Provides:       tex(beamerouterthemeUR.sty) = %{tl_version}
Provides:       tex(beamerthemeUR.sty) = %{tl_version}

%description -n texlive-urcls
The bundle provides a beamer-derived class and a theme style
file for the corporate design of the University of Regensburg.
It also contains a scrlttr2-derived class for letters using the
corporate design of the UR. Users may use the class itself
(URbeamer) or use the theme in the usual way with
\usetheme{UR}. Examples of using both letters and presentations
are provided as .tex and .pdf-files.

%package -n texlive-urcls-doc
Summary:        Documentation for urcls
Version:        svn43734
Provides:       tex-urcls-doc
AutoReqProv:    No

%description -n texlive-urcls-doc
Documentation for urcls

%package -n texlive-uowthesis
Provides:       tex-uowthesis = %{tl_version}
License:        LPPL 1.3
Summary:        Document class for dissertations at the University of Wollongong
Version:        svn19700.1.0a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(geometry.sty), tex(fancyhdr.sty), tex(setspace.sty), tex(graphicx.sty)
Requires:       tex(nextpage.sty), tex(hyperref.sty)
Provides:       tex(UoWthesis.cls) = %{tl_version}

%description -n texlive-uowthesis
A document class for higher degree research theses in
compliance with the specifications of University of Wollongong
(UoW) theses in the "Guidelines for Preparation and Submission
of Higher Degree Research Theses" (March 2006), by the Research
Student Centre, Research & Innovation Division, UoW.

%package -n texlive-uowthesis-doc
Summary:        Documentation for uowthesis
Version:        svn19700.1.0a

Provides:       tex-uowthesis-doc
AutoReqProv:    No

%description -n texlive-uowthesis-doc
Documentation for uowthesis

%package -n texlive-uowthesistitlepage
Provides:       tex-uowthesistitlepage = %{tl_version}
License:        LPPL 1.3
Summary:        Title page for dissertations at the University of Wollongong
Version:        svn45022
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(geometry.sty), tex(setspace.sty), tex(etoolbox.sty), tex(graphicx.sty)
Provides:       tex(uowthesistitlepage.sty) = %{tl_version}

%description -n texlive-uowthesistitlepage
The package redefines \maketitle to generate a title page for a
University of Wollongong thesis, in accordance with the UoW
branding guidelines. The package should be used with the book
class to typeset a thesis. The package also defines a
\declaration command that typesets the declaration that this
thesis is your own work, etc., which is required in the front
of each PhD Thesis.

%package -n texlive-uowthesistitlepage-doc
Summary:        Documentation for uowthesistitlepage
Version:        svn45022
Provides:       tex-uowthesistitlepage-doc
AutoReqProv:    No

%description -n texlive-uowthesistitlepage-doc
Documentation for uowthesistitlepage

%package -n texlive-uspatent
Provides:       tex-uspatent = %{tl_version}
License:        LPPL 1.3
Summary:        U.S. Patent Application Tools for LaTeX and LyX
Version:        svn27744.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(uspatent.cls) = %{tl_version}

%description -n texlive-uspatent
The package provides a class and other tools for developing a
beautifully formatted, consistent U.S. Patent Application using
LaTeX and/or LyX.

%package -n texlive-uspatent-doc
Summary:        Documentation for uspatent
Version:        svn27744.1.0

Provides:       tex-uspatent-doc
AutoReqProv:    No

%description -n texlive-uspatent-doc
Documentation for uspatent

%package -n texlive-ut-thesis
Provides:       tex-ut-thesis = %{tl_version}
License:        LPPL 1.3
Summary:        University of Toronto thesis style
Version:        svn38269.2.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty), tex(geometry.sty), tex(setspace.sty)
Provides:       tex(ut-thesis.cls) = %{tl_version}

%description -n texlive-ut-thesis
This not described as an 'official' class, just one distributed
"in the hope that it will be useful". A skeleton file, using
the class, is provided.

%package -n texlive-ut-thesis-doc
Summary:        Documentation for ut-thesis
Version:        svn38269.2.1

Provides:       tex-ut-thesis-doc
AutoReqProv:    No

%description -n texlive-ut-thesis-doc
Documentation for ut-thesis

%package -n texlive-uwthesis
Provides:       tex-uwthesis = %{tl_version}
License:        ASL 2.0
Summary:        University of Washington thesis class
Version:        svn15878.6.13

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(uwthesis.cls) = %{tl_version}

%description -n texlive-uwthesis
uwthesis package

%package -n texlive-uwthesis-doc
Summary:        Documentation for uwthesis
Version:        svn15878.6.13

Provides:       tex-uwthesis-doc
AutoReqProv:    No

%description -n texlive-uwthesis-doc
Documentation for uwthesis

%package -n texlive-vancouver
Provides:       tex-vancouver = %{tl_version}
License:        LPPL 1.3
Summary:        Bibliographic style file for Biomedical Journals
Version:        svn34470.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-vancouver
This BibTeX style file is generated with the docstrip utility
and modified manually to meet the Uniform Requirements for
Manuscripts Submitted to Biomedical Journals as published in N
Engl J Med 1997;336:309-315 (also known as the Vancouver
style). The complete set of requirements may be viewed on the
ICMJE web site.

%package -n texlive-vancouver-doc
Summary:        Documentation for vancouver
Version:        svn34470.0

Provides:       tex-vancouver-doc
AutoReqProv:    No

%description -n texlive-vancouver-doc
Documentation for vancouver

%package -n texlive-wsemclassic
Provides:       tex-wsemclassic = %{tl_version}
License:        BSD
Summary:        LaTeX class for Bavarian school w-seminar papers
Version:        svn31532.1.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty), tex(iftex.sty), tex(inputenx.sty), tex(fontenc.sty)
Requires:       tex(babel.sty), tex(babelbib.sty), tex(polyglossia.sty), tex(fontspec.sty)
Requires:       tex(hyperref.sty), tex(microtype.sty), tex(amsmath.sty), tex(amsthm.sty)
Requires:       tex(amssymb.sty), tex(titlesec.sty), tex(natbib.sty), tex(setspace.sty)
Requires:       tex(geometry.sty), tex(fancyhdr.sty), tex(tocbibind.sty), tex(soulutf8.sty)
Provides:       tex(wsemclassic.cls) = %{tl_version}

%description -n texlive-wsemclassic
The class is designed either to conform with the
recommendations of the Bavarian Kultusministerium for
typesetting w-seminar papers (strict mode), or to use another
style which should look better. The class is based on the LaTeX
standard report class.

%package -n texlive-wsemclassic-doc
Summary:        Documentation for wsemclassic
Version:        svn31532.1.0.1

Provides:       tex-wsemclassic-doc
AutoReqProv:    No

%description -n texlive-wsemclassic-doc
Documentation for wsemclassic

%package -n texlive-unitsdef
Provides:       tex-unitsdef = %{tl_version}
License:        LPPL
Summary:        Typesetting units in LaTeX
Version:        svn15878.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fontenc.sty), tex(amsmath.sty), tex(textcomp.sty), tex(units.sty)
Requires:       tex(xspace.sty)
Provides:       tex(ampabbrv.cfg) = %{tl_version}, tex(enerabbr.cfg) = %{tl_version}
Provides:       tex(freqabbr.cfg) = %{tl_version}, tex(lengabbr.cfg) = %{tl_version}
Provides:       tex(molabbrv.cfg) = %{tl_version}, tex(timeabbr.cfg) = %{tl_version}
Provides:       tex(unitsdef.sty) = %{tl_version}, tex(volabbrv.cfg) = %{tl_version}
Provides:       tex(voltabbr.cfg) = %{tl_version}, tex(weigabbr.cfg) = %{tl_version}

%description -n texlive-unitsdef
Many packages for typesetting units have been written for use
in LaTeX2e. Some define macros to typeset a lot of units but do
not suit to the actual font settings, some make the characters
needed available but do not predefine any unit. This package
tries to comply with both requirements. It predefines common
units, defines an easy to use interface to define new units and
changes the output concerning to the surrounding font settings.

%package -n texlive-unitsdef-doc
Summary:        Documentation for unitsdef
Version:        svn15878.0.2

Provides:       tex-unitsdef-doc
AutoReqProv:    No

%description -n texlive-unitsdef-doc
Documentation for unitsdef

%package -n texlive-ucharclasses
Provides:       tex-ucharclasses = %{tl_version}
License:        Public Domain
Summary:        Font actions in XeTeX according to what is being processed
Version:        svn45024
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifxetex.sty)
Provides:       tex(ucharclasses.sty) = %{tl_version}

%description -n texlive-ucharclasses
The package takes care of switching fonts when you switch from
one Unicode block to another in the text of a document. This
way, you can write a document with no explicit font selection,
but a series of rules of the form "when entering block ...,
switch font to use ...".

%package -n texlive-ucharclasses-doc
Summary:        Documentation for ucharclasses
Version:        svn45024
Provides:       tex-ucharclasses-doc
AutoReqProv:    No

%description -n texlive-ucharclasses-doc
Documentation for ucharclasses

%package -n texlive-unisugar
Provides:       tex-unisugar = %{tl_version}
License:        LPPL 1.3
Summary:        Define syntactic sugar for Unicode LaTeX
Version:        svn22357.0.92

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifxetex.sty)
Provides:       tex(unisugar.sty) = %{tl_version}

%description -n texlive-unisugar
The package allows the user to define shorthand aliases for
single Unicode characters, and also provides support for such
aliases in RTL-text. The package requires an TeX-alike system
that uses Unicode input in a native way: current examples are
XeTeX and LuaTeX.

%package -n texlive-unisugar-doc
Summary:        Documentation for unisugar
Version:        svn22357.0.92

Provides:       tex-unisugar-doc
AutoReqProv:    No

%description -n texlive-unisugar-doc
Documentation for unisugar

%package -n texlive-uantwerpendocs-doc
Provides:       tex-uantwerpendocs-doc = %{tl_version}
License:        LPPL
Summary:        doc files of uantwerpendocs
Version:        svn48061
AutoReqProv:    No

%description -n texlive-uantwerpendocs-doc
Documentation for uantwerpendocs.

%package -n texlive-uantwerpendocs
Provides:       tex-uantwerpendocs = %{tl_version}
License:        LPPL
Summary:        Course texts and masters theses in University of Antwerp style
Version:        svn48061

%description -n texlive-uantwerpendocs
These class files implement the house style of the University
of Antwerp for course texts, master theses, and letters. Using
these class files will make it easy for you to make and keep
your documents compliant to this version and future versions of
the house style of the University of Antwerp.

%package -n texlive-uhrzeit-doc
Provides:       tex-uhrzeit-doc = %{tl_version}
License:        LPPL
Summary:        doc files of uhrzeit
Version:        svn39570

AutoReqProv:    No

%description -n texlive-uhrzeit-doc
Documentation for uhrzeit

%package -n texlive-uhrzeit
Provides:       tex-uhrzeit = %{tl_version}
License:        LPPL
Summary:        Time printing, in German
Version:        svn39570

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(uhrzeit.sty) = %{tl_version}

%description -n texlive-uhrzeit
The primary goal of this package is to facilitate formats and
ranges of times as formerly used in Germany. A variety of
printing formats are available.

%package -n texlive-umbclegislation-doc
Provides:       tex-umbclegislation-doc = %{tl_version}
License:        GPLv3+
Summary:        doc files of umbclegislation
Version:        svn41348

AutoReqProv:    No

%description -n texlive-umbclegislation-doc
Documentation for umbclegislation

%package -n texlive-umbclegislation
Provides:       tex-umbclegislation = %{tl_version}
License:        GPLv3+
Summary:        class for building legislation files for UMBC Student Government Association Bills
Version:        svn41348

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(legislation.cls) = %{tl_version}

%description -n texlive-umbclegislation
LaTeX class for building legislation files for UMBC Student
Government Association Bills. Requires pdflatex and the
mdframed enumitem, lineno, and xifthen packages.

%package -n texlive-unicode-data-doc
Provides:       tex-unicode-data-doc = %{tl_version}
License:        LPPL and Unicode
Summary:        doc files of unicode-data
Version:        svn48003
AutoReqProv:    No

%description -n texlive-unicode-data-doc
Documentation for unicode-data

%package -n texlive-unicode-data
Provides:       tex-unicode-data = %{tl_version}
License:        LPPL and Unicode
Summary:        Unicode data and loaders for TeX
Version:        svn48003
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(load-unicode-math-classes.tex) = %{tl_version}
Provides:       tex(load-unicode-data.tex) = %{tl_version}
Provides:       tex(load-unicode-xetex-classes.tex) = %{tl_version}

%description -n texlive-unicode-data
This bundle provides generic access to Unicode Consortium data
for TeX use. It contains a set of text files provided by the
Unicode Consortium which are currently all from Unicode 8.0.0,
with the exception of MathClass.txt which is not currently part
of the Unicode Character Database. Accompanying these source
data are generic TeX loader files allowing this data to be used
as part of TeX runs, in particular in building format files.
Currently there are two loader files: one for general character
set up and one for initialising XeTeX character classes as has
been carried out to date by unicode-letters.tex. The source
data are distributed in accordance with the license stipulated
by the Unicode Consortium. The bundle as a whole is co-
ordinated by the LaTeX3 Project as a general resource for TeX
users.

%package -n texlive-updmap-map
Provides:       tex-updmap-map = %{tl_version}
License:        Public Domain
Summary:        Font maps
Version:        svn48150
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(pdftex_dl14.map) = %{tl_version}, tex(pdftex.map) = %{tl_version}
Provides:       tex(pdftex_ndl14.map) = %{tl_version}, tex(psfonts.map) = %{tl_version}
Provides:       tex(psfonts_pk.map) = %{tl_version}, tex(psfonts_t1.map) = %{tl_version}
Provides:       tex(ps2pk.map) = %{tl_version}, tex(download35.map) = %{tl_version}
Provides:       tex(builtin35.map) = %{tl_version}, tex(kanjix.map) = %{tl_version}

%description -n texlive-updmap-map
Font maps.

%package -n texlive-uplatex
Provides:       tex-uplatex = %{tl_version}
License:        BSD
Summary:        pLaTeX2e and miscellaneous macros for upTeX
Version:        svn48294
Requires:       texlive-babel, texlive-base, texlive-cm, texlive-hyphen-base
Requires:       texlive-kpathsea-bin, tex-kpathsea, texlive-latex, texlive-latex-fonts
Requires:       texlive-uptex-fonts, texlive-uptex, texlive-uplatex-bin
Provides:       tex(utbook.cls) = %{tl_version}, tex(utreport.cls) = %{tl_version}
Provides:       tex(ujreport.cls) = %{tl_version}, tex(ujarticle.cls) = %{tl_version}
Provides:       tex(utarticle.cls) = %{tl_version}, tex(ujbook.cls) = %{tl_version}
Provides:       tex(uptrace.sty) = %{tl_version}, tex(ukinsoku.tex) = %{tl_version}
Provides:       tex(jt2gt.fd) = %{tl_version}, tex(jt2mc.fd) = %{tl_version}
Provides:       tex(jy2gt.fd) = %{tl_version}, tex(jy2mc.fd) = %{tl_version}
Provides:       tex(utsize11.clo) = %{tl_version}, tex(ujbk12.clo) = %{tl_version}
Provides:       tex(utbk10.clo) = %{tl_version}, tex(utbk11.clo) = %{tl_version}
Provides:       tex(utsize10.clo) = %{tl_version}, tex(ujbk10.clo) = %{tl_version}
Provides:       tex(utbk12.clo) = %{tl_version}, tex(ujbk11.clo) = %{tl_version}
Provides:       tex(ujsize10.clo) = %{tl_version}, tex(ujsize12.clo) = %{tl_version}
Provides:       tex(ujsize11.clo) = %{tl_version}, tex(utsize12.clo) = %{tl_version}

%description -n texlive-uplatex
The bundle provides pLaTeX2e macros for upTeX by Takuji Tanaka.
This is a community edition syncing with platex.

%package -n texlive-visualpstricks-doc
Provides:       tex-visualpstricks-doc = %{tl_version}
License:        GPL+
Summary:        doc files of visualpstricks
Version:        svn39799

AutoReqProv:    No

%description -n texlive-visualpstricks-doc
Documentation for visualpstricks

%package -n texlive-visualtikz-doc
Provides:       tex-visualtikz-doc = %{tl_version}
License:        LPPL
Summary:        doc files of visualtikz
Version:        svn43239
AutoReqProv:    No

%description -n texlive-visualtikz-doc
Documentation for visualtikz

%package -n texlive-ucsmonograph
Summary:        Typesetting academic documents from the University of Caxias do Sul
Version:        svn48438
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(ucsmonograph.cls) = %{tl_version}

%description -n texlive-ucsmonograph
This is a LaTeX class for typesetting academic documents
according to the ABNT (Brazilian Technical Standards
Association) standards and the UCS (University of Caxias do
Sul) specifications.

%package -n texlive-univie-ling
Summary:        Papers, theses and research proposals in (Applied) Linguistics at Vienna University
Version:        svn47490
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(univie-ling-expose.cls) = %{tl_version}
Provides:       tex(univie-ling-paper.cls) = %{tl_version}
Provides:       tex(univie-ling-thesis.cls) = %{tl_version}
Provides:       tex(univie-ling-wlg.cls) = %{tl_version}
Provides:       tex(univie-ling.bbx) = %{tl_version}, tex(univie-ling.cbx) = %{tl_version}

%description -n texlive-univie-ling
This bundle provides LaTeX2e classes suitable for student
papers, PhD research proposals (Exposes), and theses in
(Applied) Linguistics at the University of Vienna. The classes
implement some standards for these types of text, such as
suitable title pages. They are particularly suited for the
field of (Applied) Linguistics and pre-load some packages that
are considered useful in this context. The classes can also be
used for General and Historical Linguistics as well as for
other fields of study at Vienna University. In this case,
however, some settings may have to be adjusted.

%package -n texlive-uppunctlm
Summary:        Always keep upright shape for some punctuation marks and Arabic numerals
Version:        svn42334
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(ec-uplmri10.tfm) = %{tl_version}, tex(ec-uplmri12.tfm) = %{tl_version}
Provides:       tex(ec-uplmri7.tfm) = %{tl_version}, tex(ec-uplmri8.tfm) = %{tl_version}
Provides:       tex(ec-uplmri9.tfm) = %{tl_version}, tex(ec-uplmri10.vf) = %{tl_version}
Provides:       tex(ec-uplmri12.vf) = %{tl_version}, tex(ec-uplmri7.vf) = %{tl_version}
Provides:       tex(ec-uplmri8.vf) = %{tl_version}, tex(ec-uplmri9.vf) = %{tl_version}
Provides:       tex(t1uplmr.fd) = %{tl_version}, tex(uppunctlm.sty) = %{tl_version}

%description -n texlive-uppunctlm
The package provides a mechanism to keep punctuation always in
upright shape even if italic was specified. It is directed to
Latin Modern fonts, and provides .tfm, .vf, .fd, and .sty
files. Here a list of punctuation characters always presented
in upright shapes: comma, period, semicolon, colon,
parentheses, square brackets, and Arabic numerals.

%package -n texlive-witharrows
Summary:        "Aligned" math environments with arrows for comments
Version:        svn48422
License:        LPPL
Requires:       texlive-base texlive-kpathsea, tex(expl3.sty)
Requires:       tex(footnote.sty), tex(l3keys2e.sty), tex(tikz.sty), tex(xparse.sty)
Provides:       tex(witharrows.sty) = %{tl_version}

%description -n texlive-witharrows
This package provides an environment WithArrows which is
similar to the environment aligned of amsmath (and mathtools),
but gives the possibility to draw arrows on the right side of
the alignment. These arrows are usually used to give
explanations concerning the mathematical calculus presented.
The package requires the following other LaTeX packages: expl3,
footnote, l3keys2e, tikz, and xparse.

%prep
%setup -q -c -T -a 3

%build

%install
install -d %{buildroot}%{_texdir}/../texmf
install -d %{buildroot}%{_texdir}/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf
install -d %{buildroot}%{_texdir}/texmf-dist
install -d %{buildroot}%{_texdir}/texmf-local

set +x
for i in %{sources}; do
  if [ "$i" != "%{_sourcedir}/texlive-licenses.tar.xz" ]; then
    if [ "$i" = "%{_sourcedir}/texlive-msg-translations.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/texworks.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/uplatex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.doc.tar.xz" ]; then
      OUTDIR="%{buildroot}%{_texdir}"
    else
      OUTDIR="%{buildroot}%{_texdir}/texmf-dist"
    fi
    xz -dc $i | tar x -C $OUTDIR
  fi
done
set -x

cur_dir=$PWD


install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts
font_names="arkandis/universalis public/umtypewriter"
for i in ${font_names}; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
cd $cur_dir


install -d %{buildroot}/%{_infodir}/
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/*
rm -f %{buildroot}%{_datadir}/texlive/tlpkg/tlpobj/uplatex.tlpobj

%files -n texlive-wadalab
%{_texdir}/texmf-dist/fonts/afm/wadalab/
%{_texdir}/texmf-dist/fonts/map/dvips/wadalab/
%{_texdir}/texmf-dist/fonts/tfm/wadalab/
%{_texdir}/texmf-dist/fonts/type1/wadalab/
%{_texdir}/texmf-dist/fonts/vf/wadalab/

%files -n texlive-wadalab-doc
%{_texdir}/texmf-dist/doc/fonts/wadalab/

%files -n texlive-uassign
%license gpl2.txt
%{_texdir}/texmf-dist/tex/latex/uassign/

%files -n texlive-uassign-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/latex/uassign/

%files -n texlive-ucharcat
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ucharcat/

%files -n texlive-ucharcat-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ucharcat/

%files -n texlive-ucs
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/ucs/

%files -n texlive-ucs-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ucs/

%files -n texlive-uhc
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/uhc/
%{_texdir}/texmf-dist/fonts/afm/uhc/
%{_texdir}/texmf-dist/fonts/map/dvips/uhc/
%{_texdir}/texmf-dist/fonts/tfm/uhc/
%{_texdir}/texmf-dist/fonts/type1/uhc/
%{_texdir}/texmf-dist/fonts/vf/uhc/

%files -n texlive-uhc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/uhc/

%files -n texlive-url
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/url/

%files -n texlive-url-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/url/

%files -n texlive-unfonts-core
%license gpl2.txt
%doc %{_texdir}/texmf-dist/doc/fonts/unfonts-core/
%{_texdir}/texmf-dist/fonts/truetype/public/unfonts-core/

%files -n texlive-unfonts-extra
%license gpl2.txt
%doc %{_texdir}/texmf-dist/doc/fonts/unfonts-extra/
%{_texdir}/texmf-dist/fonts/truetype/public/unfonts-extra/

%files -n texlive-unicode-bidi
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/xelatex/unicode-bidi/README.md
%{_texdir}/texmf-dist/tex/xelatex/unicode-bidi/unicode-bidi.sty

%files -n texlive-unitn-bimrep
%doc %{_texdir}/texmf-dist/doc/latex/unitn-bimrep/
%{_texdir}/texmf-dist/tex/latex/unitn-bimrep/

%files -n texlive-upzhkinsoku
%license knuth.txt
%doc %{_texdir}/texmf-dist/doc/generic/upzhkinsoku/
%{_texdir}/texmf-dist/tex/generic/upzhkinsoku/

%files -n texlive-uspace
%doc %{_texdir}/texmf-dist/doc/latex/uspace/
%{_texdir}/texmf-dist/tex/latex/uspace/

%files -n texlive-variablelm
%license gfl.txt
%doc %{_texdir}/texmf-dist/doc/fonts/variablelm/
%{_texdir}/texmf-dist/tex/latex/variablelm/

%files -n texlive-wallcalendar
%license lppl.txt
%doc %{_texdir}/texmf-dist/doc/lualatex/wallcalendar/
%{_texdir}/texmf-dist/tex/lualatex/wallcalendar/

%files -n texlive-wtref
%{_texdir}/texmf-dist/doc/latex/wtref/
%{_texdir}/texmf-dist/tex/latex/wtref/

%files -n texlive-uni-wtal-ger
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/uni-wtal-ger/

%files -n texlive-uni-wtal-ger-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/uni-wtal-ger/

%files -n texlive-uni-wtal-lin
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/uni-wtal-lin/

%files -n texlive-uni-wtal-lin-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/uni-wtal-lin/

%files -n texlive-usebib
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/usebib/

%files -n texlive-usebib-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/usebib/

%files -n texlive-vak
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/vak/

%files -n texlive-vak-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/bibtex/vak/

%files -n texlive-vntex
%{_texdir}/texmf-dist/fonts/afm/vntex/
%{_texdir}/texmf-dist/fonts/enc/dvips/vntex/
%{_texdir}/texmf-dist/fonts/enc/pdftex/vntex/
%{_texdir}/texmf-dist/fonts/map/dvips/vntex/
%{_texdir}/texmf-dist/fonts/source/vntex/
%{_texdir}/texmf-dist/fonts/tfm/vntex/
%{_texdir}/texmf-dist/fonts/type1/vntex/
%{_texdir}/texmf-dist/fonts/vf/vntex/
%{_texdir}/texmf-dist/tex/latex/vntex/
%{_texdir}/texmf-dist/tex/plain/vntex/

%files -n texlive-vntex-doc
%{_texdir}/texmf-dist/doc/generic/vntex/

%files -n texlive-ucsmonograph
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/ucsmonograph/
%doc %{_texdir}/texmf-dist/doc/latex/ucsmonograph/

%files -n texlive-univie-ling
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/univie-ling/
%doc %{_texdir}/texmf-dist/doc/latex/univie-ling/

%files -n texlive-uppunctlm
%license lppl.txt
%{_texdir}/texmf-dist/fonts/tfm/public/uppunctlm/
%{_texdir}/texmf-dist/fonts/vf/public/uppunctlm/
%{_texdir}/texmf-dist/tex/latex/uppunctlm/
%doc %{_texdir}/texmf-dist/doc/fonts/uppunctlm/

%files -n texlive-witharrows
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/witharrows/
%doc %{_texdir}/texmf-dist/doc/latex/witharrows/

%files -n texlive-ukrhyph
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/ukrhyph/

%files -n texlive-ukrhyph-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/ukrhyph/

%files -n texlive-ulem
%{_texdir}/texmf-dist/tex/generic/ulem/

%files -n texlive-ulem-doc
%{_texdir}/texmf-dist/doc/generic/ulem/

%files -n texlive-unicode-data-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/unicode-data/

%files -n texlive-unicode-data
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/unicode-data/

%files -n texlive-updmap-map
%license pd.txt
%{_texdir}/texmf-dist/fonts/map/pdftex/updmap/
%{_texdir}/texmf-dist/fonts/map/dvips/updmap/
%{_texdir}/texmf-dist/fonts/map/dvipdfmx/updmap/

%files -n texlive-uplatex
%license bsd.txt
%{_texdir}/texmf-dist/tex/uplatex/

%files -n texlive-visualpstricks-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/latex/visualpstricks/

%files -n texlive-visualtikz-doc
%license lppl.txt
%{_texdir}/texmf-dist/doc/latex/visualtikz/

%files -n texlive-utopia
%{_texdir}/texmf-dist/fonts/afm/adobe/utopia/
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/
%{_texdir}/texmf-dist/fonts/type1/adobe/utopia/
%{_texdir}/texmf-dist/fonts/vf/adobe/utopia/

%files -n texlive-utopia-doc
%{_texdir}/texmf-dist/doc/fonts/utopia/

%files -n texlive-wasy
%license pd.txt
%{_texdir}/texmf-dist/fonts/source/public/wasy/
%{_texdir}/texmf-dist/fonts/tfm/public/wasy/
%{_texdir}/texmf-dist/tex/plain/wasy/

%files -n texlive-wasy-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/fonts/wasy/

%files -n texlive-wasy2-ps
%license pd.txt
%{_texdir}/texmf-dist/fonts/afm/public/wasy2-ps/
%{_texdir}/texmf-dist/fonts/map/dvips/wasy2-ps/
%{_texdir}/texmf-dist/fonts/type1/public/wasy2-ps/

%files -n texlive-wasy2-ps-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/fonts/wasy2-ps/

%files -n texlive-wasysym
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/wasysym/

%files -n texlive-wasysym-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/wasysym/

%files -n texlive-universa
%license gpl.txt
%{_texdir}/texmf-dist/fonts/source/public/universa/
%{_texdir}/texmf-dist/fonts/tfm/public/universa/
%{_texdir}/texmf-dist/tex/latex/universa/

%files -n texlive-universa-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/universa/

%files -n texlive-universalis
%license gpl2.txt
%{_datadir}/fonts/universalis
%{_texdir}/texmf-dist/fonts/enc/dvips/universalis/
%{_texdir}/texmf-dist/fonts/map/dvips/universalis/
%{_texdir}/texmf-dist/fonts/opentype/arkandis/universalis/
%{_texdir}/texmf-dist/fonts/tfm/arkandis/universalis/
%{_texdir}/texmf-dist/fonts/type1/arkandis/universalis/
%{_texdir}/texmf-dist/fonts/vf/arkandis/universalis/
%{_texdir}/texmf-dist/tex/latex/universalis/

%files -n texlive-universalis-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/fonts/universalis/

%files -n texlive-urwchancal
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/tfm/urw/urwchancal/
%{_texdir}/texmf-dist/fonts/vf/urw/urwchancal/
%{_texdir}/texmf-dist/tex/latex/urwchancal/

%files -n texlive-urwchancal-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/urwchancal/

%files -n texlive-venturisadf
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis/
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis2/
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturisold/
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans/
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans2/
%{_texdir}/texmf-dist/fonts/enc/dvips/venturisadf/
%{_texdir}/texmf-dist/fonts/map/dvips/venturis/
%{_texdir}/texmf-dist/fonts/map/dvips/venturis2/
%{_texdir}/texmf-dist/fonts/map/dvips/venturisold/
%{_texdir}/texmf-dist/fonts/map/dvips/venturissans/
%{_texdir}/texmf-dist/fonts/map/dvips/venturissans2/
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturisold/
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturisold/
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis2/
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturisold/
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans2/
%{_texdir}/texmf-dist/tex/latex/venturis/
%{_texdir}/texmf-dist/tex/latex/venturis2/
%{_texdir}/texmf-dist/tex/latex/venturisadf/
%{_texdir}/texmf-dist/tex/latex/venturisold/
%{_texdir}/texmf-dist/tex/latex/venturissans/
%{_texdir}/texmf-dist/tex/latex/venturissans2/

%files -n texlive-venturisadf-doc
%{_texdir}/texmf-dist/doc/fonts/venturisadf/

%files -n texlive-wnri
%license gpl.txt
%{_texdir}/texmf-dist/fonts/source/public/wnri/
%{_texdir}/texmf-dist/fonts/tfm/public/wnri/

%files -n texlive-wnri-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/wnri/

%files -n texlive-wnri-latex
%license gpl2.txt
%{_texdir}/texmf-dist/tex/latex/wnri-latex/

%files -n texlive-wnri-latex-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/latex/wnri-latex/

%files -n texlive-wsuipa
%{_texdir}/texmf-dist/fonts/source/public/wsuipa/
%{_texdir}/texmf-dist/fonts/tfm/public/wsuipa/
%{_texdir}/texmf-dist/tex/latex/wsuipa/

%files -n texlive-wsuipa-doc
%{_texdir}/texmf-dist/doc/fonts/wsuipa/

%files -n texlive-uafthesis
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/uafthesis/

%files -n texlive-uafthesis-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/uafthesis/

%files -n texlive-ucbthesis
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/ucbthesis/

%files -n texlive-ucbthesis-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ucbthesis/

%files -n texlive-ucdavisthesis
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ucdavisthesis/

%files -n texlive-ucdavisthesis-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ucdavisthesis/

%files -n texlive-ucthesis
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/ucthesis/

%files -n texlive-ucthesis-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ucthesis/

%files -n texlive-uestcthesis
%license lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bst/uestcthesis/
%{_texdir}/texmf-dist/tex/latex/uestcthesis/

%files -n texlive-uestcthesis-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/uestcthesis/

%files -n texlive-uiucredborder
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/uiucredborder/

%files -n texlive-uiucredborder-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/uiucredborder/

%files -n texlive-uiucthesis
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/uiucthesis/

%files -n texlive-uiucthesis-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/uiucthesis/

%files -n texlive-ulthese
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/ulthese/

%files -n texlive-ulthese-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ulthese/

%files -n texlive-umthesis
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/umthesis/

%files -n texlive-umthesis-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/umthesis/

%files -n texlive-umich-thesis
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/umich-thesis/

%files -n texlive-umich-thesis-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/umich-thesis/

%files -n texlive-unamth-template-doc
%license gpl3.txt
%{_texdir}/texmf-dist/doc/latex/unamth-template/

%files -n texlive-unamthesis
%license lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bst/unamthesis/
%{_texdir}/texmf-dist/tex/latex/unamthesis/

%files -n texlive-unamthesis-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/unamthesis/

%files -n texlive-unswcover
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/unswcover/

%files -n texlive-unswcover-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/unswcover/

%files -n texlive-uothesis
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/uothesis/

%files -n texlive-uothesis-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/uothesis/

%files -n texlive-urcls
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/urcls/

%files -n texlive-urcls-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/urcls/

%files -n texlive-uowthesis
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/uowthesis/

%files -n texlive-uowthesis-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/uowthesis/

%files -n texlive-uowthesistitlepage
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/uowthesistitlepage/

%files -n texlive-uowthesistitlepage-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/uowthesistitlepage/

%files -n texlive-uspatent
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/uspatent/

%files -n texlive-uspatent-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/uspatent/

%files -n texlive-ut-thesis
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/ut-thesis/

%files -n texlive-ut-thesis-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ut-thesis/

%files -n texlive-uwthesis
%license apache2.txt
%{_texdir}/texmf-dist/tex/latex/uwthesis/

%files -n texlive-uwthesis-doc
%license apache2.txt
%{_texdir}/texmf-dist/doc/latex/uwthesis/

%files -n texlive-vancouver
%license lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bst/vancouver/

%files -n texlive-vancouver-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/bibtex/vancouver/

%files -n texlive-verbatimbox
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/verbatimbox/

%files -n texlive-verbatimbox-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/verbatimbox/

%files -n texlive-verbatimcopy
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/verbatimcopy/

%files -n texlive-verbatimcopy-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/verbatimcopy/

%files -n texlive-verbdef
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/verbdef/

%files -n texlive-verbdef-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/verbdef/

%files -n texlive-verbments
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/verbments/

%files -n texlive-verbments-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/verbments/

%files -n texlive-version
%{_texdir}/texmf-dist/tex/latex/version/

%files -n texlive-version-doc
%{_texdir}/texmf-dist/doc/latex/version/

%files -n texlive-versions
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/versions/

%files -n texlive-versions-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/versions/

%files -n texlive-versonotes
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/versonotes/

%files -n texlive-versonotes-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/versonotes/

%files -n texlive-vertbars
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/vertbars/

%files -n texlive-vertbars-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/vertbars/

%files -n texlive-vgrid
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/vgrid/

%files -n texlive-vgrid-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/vgrid/

%files -n texlive-vhistory
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/vhistory/

%files -n texlive-vhistory-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/vhistory/

%files -n texlive-vmargin
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/vmargin/

%files -n texlive-vmargin-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/vmargin/

%files -n texlive-volumes
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/volumes/

%files -n texlive-volumes-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/volumes/

%files -n texlive-vruler
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/vruler/

%files -n texlive-vruler-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/vruler/

%files -n texlive-vwcol
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/vwcol/

%files -n texlive-vwcol-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/vwcol/

%files -n texlive-wallpaper
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/wallpaper/

%files -n texlive-wallpaper-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/wallpaper/

%files -n texlive-warning
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/warning/

%files -n texlive-warning-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/warning/

%files -n texlive-warpcol
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/warpcol/

%files -n texlive-warpcol-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/warpcol/

%files -n texlive-was
%license collection.txt
%{_texdir}/texmf-dist/tex/latex/was/

%files -n texlive-was-doc
%license collection.txt
%{_texdir}/texmf-dist/doc/latex/was/

%files -n texlive-widetable
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/widetable/

%files -n texlive-widetable-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/widetable/

%files -n texlive-williams
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/williams/

%files -n texlive-williams-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/williams/

%files -n texlive-withargs
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/withargs/

%files -n texlive-withargs-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/withargs/

%files -n texlive-wordlike
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/wordlike/

%files -n texlive-wordlike-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/wordlike/

%files -n texlive-wsemclassic
%license bsd.txt
%{_texdir}/texmf-dist/tex/latex/wsemclassic/

%files -n texlive-wsemclassic-doc
%license bsd.txt
%{_texdir}/texmf-dist/doc/latex/wsemclassic/

%files -n texlive-underscore
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/underscore/

%files -n texlive-underscore-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/underscore/

%files -n texlive-undolabl
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/undolabl/

%files -n texlive-undolabl-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/undolabl/

%files -n texlive-units
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/units/

%files -n texlive-units-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/units/

%files -n texlive-unravel
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/unravel/

%files -n texlive-unravel-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/unravel/

%files -n texlive-upmethodology
%license lgpl2.1.txt
%{_texdir}/texmf-dist/bibtex/bst/upmethodology/
%{_texdir}/texmf-dist/tex/latex/upmethodology/

%files -n texlive-upmethodology-doc
%license lgpl2.1.txt
%{_texdir}/texmf-dist/doc/latex/upmethodology/

%files -n texlive-upquote
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/upquote/

%files -n texlive-upquote-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/upquote/

%files -n texlive-uptex-fonts
%license bsd.txt
%{_texdir}/texmf-dist/fonts/cmap/uptex-fonts/
%{_texdir}/texmf-dist/fonts/source/uptex-fonts/
%{_texdir}/texmf-dist/fonts/tfm/uptex-fonts/
%{_texdir}/texmf-dist/fonts/vf/uptex-fonts/

%files -n texlive-uptex-fonts-doc
%license bsd.txt
%{_texdir}/texmf-dist/doc/fonts/uptex-fonts/

%files -n texlive-uptex-base
%license bsd.txt
%{_texdir}/texmf-dist/tex/uptex/uptex-base/

%files -n texlive-uptex-base-doc
%license bsd.txt
%{_texdir}/texmf-dist/doc/uptex/uptex-base/

%files -n texlive-uri
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/uri/

%files -n texlive-uri-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/uri/

%files -n texlive-ushort
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ushort/

%files -n texlive-ushort-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ushort/

%files -n texlive-varindex
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/varindex/

%files -n texlive-varindex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/varindex/

%files -n texlive-varsfromjobname
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/varsfromjobname/

%files -n texlive-varsfromjobname-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/varsfromjobname/

%files -n texlive-varwidth
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/varwidth/

%files -n texlive-varwidth-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/varwidth/

%files -n texlive-vdmlisting
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/vdmlisting/

%files -n texlive-vdmlisting-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/vdmlisting/

%files -n texlive-verbasef
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/verbasef/

%files -n texlive-verbasef-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/verbasef/

%files -n texlive-wrapfig
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/wrapfig/

%files -n texlive-wrapfig-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/wrapfig/

%files -n texlive-variations
%license gpl.txt
%{_texdir}/texmf-dist/tex/generic/variations/

%files -n texlive-variations-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/generic/variations/

%files -n texlive-vaucanson-g
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/vaucanson-g/

%files -n texlive-vaucanson-g-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/vaucanson-g/

%files -n texlive-vocaltract
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/vocaltract/

%files -n texlive-vocaltract-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/vocaltract/

%files -n texlive-uaclasses
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/uaclasses/

%files -n texlive-uaclasses-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/uaclasses/

%files -n texlive-uantwerpendocs-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/uantwerpendocs/

%files -n texlive-uantwerpendocs
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/uantwerpendocs/

%files -n texlive-uhrzeit-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/uhrzeit/

%files -n texlive-uhrzeit
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/uhrzeit/

%files -n texlive-umbclegislation-doc
%license gpl3.txt
%{_texdir}/texmf-dist/doc/latex/umbclegislation/

%files -n texlive-umbclegislation
%license gpl3.txt
%{_texdir}/texmf-dist/tex/latex/umbclegislation/

%files -n texlive-udesoftec
%license lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bst/udesoftec/
%{_texdir}/texmf-dist/tex/latex/udesoftec/

%files -n texlive-udesoftec-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/udesoftec/

%files -n texlive-upca
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/upca/

%files -n texlive-upca-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/upca/

%files -n texlive-uebungsblatt
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/uebungsblatt/

%files -n texlive-uebungsblatt-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/uebungsblatt/

%files -n texlive-uhhassignment
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/uhhassignment/
%{_texdir}/texmf-dist/tex/latex/uhhassignment/

%files -n texlive-undergradmath-doc
%doc %{_texdir}/texmf-dist/doc/latex/undergradmath/

%files -n texlive-uml
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/uml/

%files -n texlive-uml-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/uml/

%files -n texlive-umlaute
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/umlaute/

%files -n texlive-umlaute-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/umlaute/

%files -n texlive-umoline
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/umoline/

%files -n texlive-umoline-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/umoline/

%files -n texlive-underlin
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/underlin/

%files -n texlive-underlin-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/underlin/

%files -n texlive-underoverlap
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/underoverlap/

%files -n texlive-underoverlap-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/underoverlap/

%files -n texlive-unicode-math
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/unicode-math/

%files -n texlive-unicode-math-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/unicode-math/

%files -n texlive-unitsdef
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/unitsdef/

%files -n texlive-unitsdef-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/unitsdef/

%files -n texlive-venndiagram
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/venndiagram/

%files -n texlive-venndiagram-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/venndiagram/

%files -n texlive-verse
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/verse/

%files -n texlive-verse-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/verse/

%files -n texlive-webguide-doc
%{_texdir}/texmf-dist/doc/latex/webguide/

%files -n texlive-visualfaq-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/visualfaq/

%files -n texlive-voss-mathcol-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/voss-mathcol/

%files -n texlive-utf8mex
%license pd.txt
%{_texdir}/texmf-dist/tex/mex/utf8mex/

%files -n texlive-utf8mex-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/mex/utf8mex/

%files -n texlive-venn
%license lppl1.txt
%{_texdir}/texmf-dist/metapost/venn/

%files -n texlive-venn-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/metapost/venn/

%files -n texlive-varisize
%license pd.txt
%{_texdir}/texmf-dist/tex/plain/varisize/

%files -n texlive-varisize-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/plain/varisize/

%files -n texlive-ucharclasses
%license pd.txt
%{_texdir}/texmf-dist/tex/xelatex/ucharclasses/

%files -n texlive-ucharclasses-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/xelatex/ucharclasses/

%files -n texlive-unisugar
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/xelatex/unisugar/

%files -n texlive-unisugar-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/xelatex/unisugar/

%files -n texlive-umtypewriter
%{_datadir}/fonts/umtypewriter
%{_texdir}/texmf-dist/fonts/opentype/public/umtypewriter/




%changelog
* Wed May 19 2021 maminjie <maminjie1@huawei.com> - 8:2018-24
- split texlive

* Fri Sep 11 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 8:2018-23
- Drop texlive-texinfo,use new files in texinfo-tex instead

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 8:2018-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Tue Dec 10 2019 Jiangping Hu <hujiangping@huawei.com> - 8:2018-21
- Package init
