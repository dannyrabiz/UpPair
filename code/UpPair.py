def make_axis(num):
    xaxis = []
    skip = 0 
    for i in list(range(num*4)): 
        if skip  < 2: 
            xaxis.append(i)
            skip +=1
        elif skip == 2:
            skip +=1
        elif skip ==3: 
            skip =0
    JIpos = arange(0.5, max(xaxis)+0.5, 4)   
    return xaxis, JIpos
    
   
def UpPair(df, vspacing = 0, title='UpPair',title_fontsize =18, plot_type='scatter', point_color = 'black',
          marker = "^", upper_ylabel = "Jaccard Index", upper_color = 'red', upper_legend = False, connected = 'None',
          upper_ymin = 0.5, upper_ymax = 1, lower_color = 'green', color1 ='lightgreen', color2 = None, 
          lower_ylabel = None, lower_xlabel = 'Samples', tick_labels = None, intersection_width = 2.5,
          intersection_label = None, label1 = None, label2 = None, style = 'ggplot'):
    plt.style.use(style)
    fig = plt.figure()
    fig.set_figheight(10)
    fig.set_figwidth(18)
    xaxis, JIpos = make_axis(df.shape[0])
    spec = gridspec.GridSpec(ncols=1, nrows=2,
                             width_ratios=[1], wspace=0.1,
                             hspace=vspacing, height_ratios=[1, 2])
    twin1 = fig.add_subplot(spec[0])
    plt.title(title, fontsize=title_fontsize)
    p2 = twin1.plot(JIpos, df['JI'], label=upper_ylabel, color = point_color, 
                        marker = marker, linestyle = connected, markersize=12)
    twin1.set_ylabel(upper_ylabel, fontsize=14)
    twin1.yaxis.label.set_color(upper_color)
    twin1.tick_params(axis='y', colors=upper_color, labelsize=14 )
    if upper_legend==True:
        twin1.legend()
    #SHADING

    twin1.set_ylim(upper_ymin, upper_ymax)  #Also change this
    alph =0.1
    grades = (upper_ymax-upper_ymin)/5
    for h in range(1,6):
        twin1.axhspan(upper_ymin+((h-1)*grades), upper_ymin+(h*grades), alpha=alph, lw=0, color=upper_color)
        alph +=0.14
    
    twin1.tick_params(axis ='x',bottom = False)
    twin1.set_xticklabels( [])

    if color2==None: 
        color2=color1
    ax = fig.add_subplot(spec[1])
    ax.bar(xaxis[::2], df['P1'], color = color1, 
           label = label1, edgecolor='black', alpha = 0.7, linewidth = 1)
    ax.bar(xaxis[1:][::2], df['P2'], color = color2, 
           label = label2, edgecolor='black', alpha = 0.7, linewidth = 1)
    ax.bar(JIpos, df['Intersection'], width = intersection_width, alpha =0.7, color =lower_color, 
           edgecolor='black', label = intersection_label)
    ax.legend()
    ax.set_xticks(JIpos)
    ax.tick_params(axis='y', colors=lower_color , labelsize=14 )
    ax.yaxis.label.set_color(lower_color)
    ax.set_ylabel(lower_ylabel, fontsize=18)
    ax.set_xlabel(lower_xlabel, fontsize=18)
    ax.set_xticklabels( tick_labels, rotation =45)


    plt.show()

def Stacked_UpPair(left1, right1,left2, right2, int1, int2,var1, var2,  vspacing = 0,shading = True, title='UpPair',title_fontsize =18, plot_type='scatter', point_color = 'black',
          marker = "^", upper_label1 = None, upper_label2 = None, upper_ylabel=None, upper_color = 'red', upper_legend = False, connected = 'None',
          upper_ymin = 0.5, upper_ymax = 1, lower_color = 'green', color1 ='lightgreen', color2 = None, int1_color = None, int2_color = None,
          lower_ylabel = None, lower_xlabel = 'Samples', tick_labels = None, intersection_width = 2.5,
          int1_label = None,int2_label = None, label1 = None, label2 = None, style ='ggplot'):
    plt.style.use(style)
    fig = plt.figure()
    fig.set_figheight(10)
    fig.set_figwidth(18)
    xaxis, JIpos = make_axis(len(left1))
    spec = gridspec.GridSpec(ncols=1, nrows=2,
                             width_ratios=[1], wspace=0.1,
                             hspace=vspacing, height_ratios=[1, 2])
    twin1 = fig.add_subplot(spec[0])
    plt.title(title, fontsize=title_fontsize)
    p1 = twin1.plot(JIpos, var1, label=upper_label1, color = int1_color, 
                        marker = marker, linestyle = connected, markersize=12)
    p2 = twin1.plot(JIpos, var2, label=upper_label2, color = int2_color, 
                        marker = marker, linestyle = connected, markersize=12)
    twin1.set_ylabel(upper_ylabel, fontsize=14)
    twin1.yaxis.label.set_color(upper_color)
    twin1.tick_params(axis='y', colors=upper_color, labelsize=14 )
    if upper_legend==True:
        twin1.legend(loc=(0.9,0.8))
    #SHADING
    if shading==True:
        twin1.set_ylim(upper_ymin, upper_ymax)  #Also change this
        alph =0.1
        grades = (upper_ymax-upper_ymin)/5
        for h in range(1,6):
            twin1.axhspan(upper_ymin+((h-1)*grades), upper_ymin+(h*grades), alpha=alph, lw=0, color=upper_color)
            alph +=0.14
    
    twin1.tick_params(axis ='x',bottom = False)
    twin1.set_xticklabels( [])
    
    twin1.spines['bottom'].set_visible(True)

    if color2==None: 
        color2=color1
    ax = fig.add_subplot(spec[1])
    ax.bar(xaxis[::2], left1, color = color1, 
           label = label1, edgecolor='None', alpha = 0.7, linewidth = 1)
    ax.bar(xaxis[1:][::2], right1, color = color1, 
           label = label2, edgecolor='None', alpha = 0.7, linewidth = 1)
    
    #stacked bar
    ax.bar(xaxis[::2], left2, color = color2, bottom = left1,
           label = label1, edgecolor='None', alpha = 0.7, linewidth = 1)
    ax.bar(xaxis[1:][::2], right2, color = color2, bottom = right1,
           label = label2, edgecolor='None', alpha = 0.7, linewidth = 1)
    #intersection
    ax.bar(JIpos, int1, width = intersection_width, alpha =1, edgecolor = int1_color, 
           color=int1_color, label = int1_label, linewidth=1)
    ax.bar(JIpos, int2,bottom = int1, width = intersection_width, alpha =1, edgecolor =int2_color, 
           color=int2_color, label = int2_label, linewidth = 1)
    
    
    ax.spines['top'].set_visible(False)
    
    ax.legend()
    ax.set_xticks(JIpos)
    ax.tick_params(axis='y', colors=lower_color , labelsize=14 )
    ax.yaxis.label.set_color(lower_color)
    ax.set_ylabel(lower_ylabel, fontsize=18)
    ax.set_xlabel(lower_xlabel, fontsize=18)
    ax.set_xticklabels( tick_labels, rotation =45)
    plt.show()

def make_trio_axis(num):
    xaxis = []
    skip = 0 
    for i in list(range(num*5)): 
        if skip  < 3: 
            xaxis.append(i)
            skip +=1
        elif skip == 3:
            skip +=1
        elif skip ==4: 
            skip =0
    JIpos = arange(1, max(xaxis)+0.5, 5)   
    return xaxis, JIpos
    
def Trio_UpPair(df, vspacing = 0, title='UpPair',title_fontsize =18, plot_type='scatter', point_color = 'black',
          marker = "^", upper_ylabel = "Jaccard Index", upper_color = 'red', upper_legend = False, connected = 'None',
          upper_ymin = 0.5, upper_ymax = 1, lower_color = 'green', color1 ='lightgreen', color2 = None, color3 = None, 
          lower_ylabel = None, lower_xlabel = 'Samples', tick_labels = None, intersection_width = 2.5,
          intersection_label = None, label1 = None, label2 = None,label3 = None, style = 'ggplot',
                int_color = 'green', int_edgecolor='black'):
    plt.style.use(style)
    fig = plt.figure()
    fig.set_figheight(10)
    fig.set_figwidth(18)
    xaxis, JIpos = make_trio_axis(df.shape[0])
    spec = gridspec.GridSpec(ncols=1, nrows=2,
                             width_ratios=[1], wspace=0.1,
                             hspace=vspacing, height_ratios=[1, 2])
    twin1 = fig.add_subplot(spec[0])
    plt.title(title, fontsize=title_fontsize)
    p2 = twin1.plot(JIpos, df['JI'], label=upper_ylabel, color = point_color, 
                        marker = marker, linestyle = connected, markersize=12)
    #right side 
    twin1.yaxis.tick_right()
    twin1.yaxis.set_label_position("right")
    
    
    twin1.set_ylabel(upper_ylabel, fontsize=14)
    twin1.yaxis.label.set_color('black')
    twin1.tick_params(axis='y', colors='black', labelsize=14 )
    if upper_legend==True:
        twin1.legend()
    #SHADING

    twin1.set_ylim(upper_ymin, upper_ymax)  #Also change this
    alph =0.1
    grades = (upper_ymax-upper_ymin)/5
    for h in range(1,6):
        twin1.axhspan(upper_ymin+((h-1)*grades), upper_ymin+(h*grades), alpha=alph, lw=0, color=upper_color)
        alph +=0.14
    
    twin1.tick_params(axis ='x',bottom = False)
    twin1.set_xticklabels( [])

    if color2==None: 
        color2=color1
    ax = fig.add_subplot(spec[1])
    ax.bar(xaxis[::3], df['P1'], color = color1, 
           label = label1, edgecolor='black', alpha = 0.7, linewidth = 1)
    ax.bar(xaxis[1:][::3], df['P2'], color = color2, 
           label = label2, edgecolor='black', alpha = 0.7, linewidth = 1)
    ax.bar(xaxis[2:][::3], df['P3'], color = color3, 
           label = label3, edgecolor='black', alpha = 0.7, linewidth = 1)
    ax.bar(JIpos, df['Intersection'], width = intersection_width, alpha =0.7, color =int_color, 
           edgecolor=int_edgecolor, label = intersection_label, linewidth = 3.5)
    
    for h, n, ind in zip(heights, names, range(36)):
        plt.text(xaxis[ind]-.3,5, n , rotation=90)
        
    
    ax.legend(fontsize = 17)
    ax.set_xticks(JIpos)
    ax.tick_params(axis='y', colors=lower_color , labelsize=14 )
    ax.yaxis.label.set_color(lower_color)
    ax.set_ylabel(lower_ylabel, fontsize=18)
    ax.set_xlabel(lower_xlabel, fontsize=18)
    ax.set_xticklabels( tick_labels, rotation =45)


    plt.show()


def Tracking_UpPair(df, vspacing = 0, title='UpPair',title_fontsize =18, plot_type='scatter', point_color = 'black',
          marker = "^", upper_ylabel = 'Sensitivity', upper_ylabel1 = "Jaccard Index",upper_ylabel2 = "Jaccard Index", upper_color = 'red', upper_legend = False, connected = 'None',
          upper_ymin = 0.5, upper_ymax = 1, lower_color = 'green', color1 ='lightgreen', color2 = None, color3 = None, 
          lower_ylabel = None, lower_xlabel = 'Samples', tick_labels = None, intersection_width = 2.5,
          intersection_label = None, label1 = None, label2 = None,label3 = None, style = 'ggplot',
                int_color = 'green', int_edgecolor='black'):
    plt.style.use(style)
    fig = plt.figure()
    fig.set_figheight(10)
    fig.set_figwidth(18)
    xaxis, JIpos = make_trio_axis(df.shape[0])
    spec = gridspec.GridSpec(ncols=1, nrows=3,
                             width_ratios=[1], wspace=0.1,
                             hspace=vspacing, height_ratios=[1, 1,3])
    twin1 = fig.add_subplot(spec[0])
    plt.title(title, fontsize=title_fontsize)
    p2 = twin1.plot(array(JIpos), df['Sensitivity1'], label=upper_ylabel, color = 'blue', 
                        marker = '^', linestyle = connected, markersize=12)
    p2 = twin1.plot(array(JIpos), df['Sensitivity2'], label=upper_ylabel, color = 'purple', 
                        marker = 'p', linestyle = 'dashed', markersize=12)
    #right side 
    #twin1.yaxis.tick_right()
    #twin1.yaxis.set_label_position("right")
    
    
    twin1.set_ylabel(upper_ylabel, fontsize=14)
    twin1.yaxis.label.set_color('black')
    twin1.tick_params(axis='y', colors='black', labelsize=14 )
    if upper_legend==True:
        twin1.legend()
    #SHADING

    twin1.set_ylim(upper_ymin, upper_ymax)  #Also change this
    alph =0.1
    grades = (upper_ymax-upper_ymin)/5
    for h in range(1,6):
        twin1.axhspan(upper_ymin+((h-1)*grades), upper_ymin+(h*grades), alpha=alph, lw=0, color=upper_color)
        alph +=0.14
    
    twin1.tick_params(axis ='x',bottom = False)
    twin1.set_xticklabels( [])
    
    
    
    #NEW
    
    twin2 = fig.add_subplot(spec[1])
    p2 = twin2.plot(array(JIpos), 1-df['Sensitivity1'], label=upper_ylabel, color = 'blue', 
                        marker = '^', linestyle = connected, markersize=12)
    p2 = twin2.plot(array(JIpos), 1-df['Sensitivity2'], label=upper_ylabel, color = 'purple', 
                        marker = 'p', linestyle = 'dashed', markersize=12)
    #right side 
    #twin1.yaxis.tick_right()
    #twin1.yaxis.set_label_position("right")
    
    
    twin2.set_ylabel('Specificity', fontsize=14)
    twin2.yaxis.label.set_color('black')
    twin2.tick_params(axis='y', colors='black', labelsize=14 )
    if upper_legend==True:
        twin2.legend()
        
    twin2.set_ylim(0, 1)  #Also change this
    alph =0.1
    grades = (1)/5
    for h in range(1,6):
        twin2.axhspan(0+((h-1)*grades), 0+(h*grades), alpha=alph, lw=0, color='red')
        alph +=0.14
    
    twin2.tick_params(axis ='x',bottom = False)
    twin2.set_xticklabels( [])
    #right side 
    twin2.yaxis.tick_right()
    twin2.yaxis.set_label_position("right")
    
    
    
    w = 1.4
    if color2==None: 
        color2=color1
    ax = fig.add_subplot(spec[2])
    ax.bar(array(xaxis[::3])-.5, df['P1'], color = 'deepskyblue', width = w, 
           label = label1, edgecolor='black', alpha = 0.7, linewidth = 0)
    ax.bar(xaxis[1:][::3], df['P2'], color = color2, width = w, 
           label = label2, edgecolor='black', alpha = 0.7, linewidth = 0)
    ax.bar(array(xaxis[2:][::3])+.5, df['P3'], color = 'violet', width = w, 
           label = label3, edgecolor='black', alpha = 0.7, linewidth = 0)
    ax.bar(JIpos-.7, df['Intersection1'], width = intersection_width, alpha =0.7, color ='blue', 
           edgecolor=int_edgecolor, label = intersection_label, linewidth = 1.5)
    ax.bar(JIpos+.7, df['Intersection2'], width = intersection_width, alpha =0.7, color ='purple', 
           edgecolor=int_edgecolor, label = intersection_label, linewidth = 1.5)
    
    #for h, n, ind in zip(heights, names, range(36)):
    #    plt.text(xaxis[ind]-.3,5, n , rotation=90)
        
    
    ax.legend(fontsize = 17)
    ax.set_xticks(JIpos)
    ax.tick_params(axis='y', colors=lower_color , labelsize=14 )
    ax.yaxis.label.set_color(lower_color)
    ax.set_ylabel(lower_ylabel, fontsize=18)
    ax.set_xlabel(lower_xlabel, fontsize=18)
    ax.set_xticklabels( tick_labels, rotation =45)
    ax.set_xlim(-2, max(xaxis)+2)

    plt.show()



def continuous_UpPair(df, vspacing = 0, title='UpPair',title_fontsize =18, plot_type='scatter', point_color = 'black',
          marker = "^", upper_ylabel = "Jaccard Index", upper_color = 'red', upper_legend = False, connected = 'None',
          upper_ymin = 0.5, upper_ymax = 1, lower_color = 'green', color1 ='lightgreen', color2 = None, 
          lower_ylabel = None, lower_xlabel = 'Samples', tick_labels = None, intersection_width = 2.5,
          intersection_label = None, label1 = None, label2 = None, style = 'ggplot'):
    plt.style.use(style)
    fig = plt.figure()
    fig.set_figheight(10)
    fig.set_figwidth(18)
    xaxis, JIpos = make_axis(df.shape[0])
    spec = gridspec.GridSpec(ncols=1, nrows=3,
                             width_ratios=[1], wspace=0.1,
                             hspace=vspacing, height_ratios=[1, 2,1])
    twin1 = fig.add_subplot(spec[0])
    plt.title(title, fontsize=title_fontsize)
    p2 = twin1.plot(JIpos, df['JI'], label=upper_ylabel, color = point_color, 
                        marker = marker, linestyle = connected, markersize=12)
    twin1.set_ylabel(upper_ylabel, fontsize=14)
    twin1.yaxis.label.set_color(upper_color)
    twin1.tick_params(axis='y', colors=upper_color, labelsize=14 )
    if upper_legend==True:
        twin1.legend()
    #SHADING

    twin1.set_ylim(upper_ymin, upper_ymax)  #Also change this
    alph =0.1
    grades = (upper_ymax-upper_ymin)/5
    for h in range(1,6):
        twin1.axhspan(upper_ymin+((h-1)*grades), upper_ymin+(h*grades), alpha=alph, lw=0, color=upper_color)
        alph +=0.14
    
    twin1.tick_params(axis ='x',bottom = False)
    twin1.set_xticklabels( [])

    if color2==None: 
        color2=color1
    ax = fig.add_subplot(spec[1])
    ax.bar(xaxis[::2], df['P1'], color = color1, 
           label = label1, edgecolor='black', alpha = 0.7, linewidth = 1)
    ax.bar(xaxis[1:][::2], df['P2'], color = color2, 
           label = label2, edgecolor='black', alpha = 0.7, linewidth = 1)
    ax.bar(JIpos, df['Intersection'], width = intersection_width, alpha =0.3, color =lower_color, 
           edgecolor='black', label = intersection_label)
    ax.legend(fontsize = 18, loc=(1,0.8), facecolor = 'None')
    
    ax.tick_params(axis='y', colors=lower_color , labelsize=14 )
    ax.yaxis.label.set_color(lower_color)
    ax.set_ylabel(lower_ylabel, fontsize=18)
    ax.set_xlim(-1.4, max(xaxis)+1.4)
    ax.set_xticklabels( [])

    
    ax1 = fig.add_subplot(spec[2])
    ax1.set_xticks(JIpos)
    ax1.set_xticks(JIpos)
    ax1.set_xlabel(lower_xlabel, fontsize=18)
    ax1.set_xticklabels( tick_labels, rotation =45)
    p1 = ax1.plot(JIpos, df['PSA'], label='Biomarker X', color = point_color, 
                        marker = '*', linestyle = 'dashed', markersize=12)
    p1 = ax1.plot(JIpos, df['Biomarker'], label='Biomarker Y', color = 'red', 
                        marker = 'd', linestyle = ':', markersize=12)
    ax1.bar(0,0, label = 'Treatment A', color = 'lightblue')
    ax1.bar(0,0, label = 'Treatment B', color = 'gray')
    ax1.bar(0,0, label = 'Treatment C', color = 'salmon')
    ax1.bar(0,0, label = 'Treatment D', color = 'palegreen')
    ax1.legend(fontsize = 18, loc=(1,0.5), facecolor = 'None')

    ax1.axvspan(JIpos[0], JIpos[2], alpha=0.5, lw=0, color='lightblue')
    ax1.axvspan(JIpos[2], JIpos[4], alpha=0.5, lw=0, color='gray') 
    ax1.axvspan(JIpos[4], JIpos[6], alpha=0.5, lw=0, color='salmon') 
    ax1.axvspan(JIpos[6], JIpos[7], alpha=0.5, lw=0, color='palegreen')
    ax1.set_ylabel('Biomarker\nLevels', fontsize=14)
    plt.show()
